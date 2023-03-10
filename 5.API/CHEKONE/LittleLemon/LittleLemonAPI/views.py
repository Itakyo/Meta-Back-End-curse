from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from django.contrib.auth.models import User, Group

from LittleLemonAPI.models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer,UserOrdersSerializer,UserSerializer,UserCartSerializer,CategorySerializer
from decimal import Decimal
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.core.paginator import Paginator, EmptyPage

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def menuitems_list(request):
    if request.method == 'GET':
        menuitems = MenuItem.objects.select_related('category').all()
        
        #search
        search = request.query_params.get('search')
        if search:
            menuitems = menuitems.filter(title__icontains=search)
        
        #ordring 
        ordering = request.query_params.get('ordering')
        if ordering:
            menuitems = menuitems.order_by(ordering)
            
        perpage = request.query_params.get('perpage',default=2)
        page = request.query_params.get('page',default=1)
        
        #Paginator
        paginator = Paginator(menuitems, per_page=perpage)
        try:
            menuitems = paginator.page(number=page)
        except EmptyPage:
            menuitems = []

        serializer_menuitems = MenuItemSerializer(menuitems, many=True)
        return Response(serializer_menuitems.data)
    
    elif request.method == 'POST':
        if request.user.groups.filter(name='Manager').exists():
            serializer_menuitems = MenuItemSerializer(data=request.data)
            serializer_menuitems.is_valid(raise_exception=True)
            serializer_menuitems.save()
            return Response(serializer_menuitems.validated_data, status=status.HTTP_201_CREATED)

        else:
                return Response({"message": "You do not have permission to Perform this action"}, status=status.HTTP_403_FORBIDDEN)
   

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def menuitem_detail(request,menuItem):
    # menuitem = MenuItem.objects.get(title=menuItem)
    menuitem = get_object_or_404(MenuItem,title=menuItem)

    if request.method == 'GET':
        serializer_menuitem = MenuItemSerializer(menuitem,many=False)
        return Response(serializer_menuitem.data)

    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'PUT':
            serializer_menuitem = MenuItemSerializer(menuitem,data=request.data)
            serializer_menuitem.is_valid(raise_exception=True)
            serializer_menuitem.save()
            return Response(serializer_menuitem.validated_data)

        if request.method == 'DELETE':
            menuitem.delete()
            return Response("Menu item Deleted! ")          
    else:
                return Response({"message": "You do not have permission to Perform this action"}, status=status.HTTP_403_FORBIDDEN)



class ManagerUsersView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # Get the 'manager' group
        manager_group = Group.objects.get(name='Manager')
        queryset = User.objects.filter(groups=manager_group)
        return queryset

    def perform_create(self, username):
        # Assign the user to the 'manager' group
        manager_group = Group.objects.get(name='Manager')
        user = username.save()
        user.groups.add(manager_group)

class ManagerSingleUserView(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        manager_group = Group.objects.get(name='Manager')
        queryset = User.objects.filter(groups=manager_group)
        return queryset

class Delivery_crew_management(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        delivery_group = Group.objects.get(name='Delivery crew')
        queryset = User.objects.filter(groups=delivery_group)
        return queryset

    def perform_create(self, serializer):
        delivery_group = Group.objects.get(name='Delivery crew')
        user = serializer.save()
        user.groups.add(delivery_group)


class Delivery_crew_management_single_view(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        delivery_group = Group.objects.get(name='Delivery crew')
        queryset = User.objects.filter(groups=delivery_group)
        return queryset



class Customer_Cart(generics.ListCreateAPIView):
    serializer_class = UserCartSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def perform_create(self, serializer):
        menuitem = self.request.data.get('menuitem')
        quantity = self.request.data.get('quantity')
        unit_price = MenuItem.objects.get(pk=menuitem).price
        quantity = int(quantity)
        price = quantity * unit_price
        serializer.save(user=self.request.user, price=price)

    def delete(self, request):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response(status=204)

class Orders_view(generics.ListCreateAPIView):
    serializer_class = UserOrdersSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    def perform_create(self, serializer):
        cart_items = Cart.objects.filter(user=self.request.user)
        total = self.calculate_total(cart_items)
        order = serializer.save(user=self.request.user, total=total)

        for cart_item in cart_items:
            OrderItem.objects.create(menuitem=cart_item.menuitem, quantity=cart_item.quantity,
                                     unit_price=cart_item.unit_price, price=cart_item.price, order=order)
            cart_item.delete()

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        return Order.objects.filter(user=user)


    def calculate_total(self, cart_items):
        total = Decimal(0)
        for item in cart_items:
            total += item.price
        return total


class Single_Order_view(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserOrdersSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        return Order.objects.filter(user=user)

    