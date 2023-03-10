#from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
     
class SingleMenuItemsView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
from rest_framework.response import Response
from rest_framework.decorators import api_view


# @api_view
# def menu_items(request):
#     items = MenuItem.objects.all()
#     return Response(items.values())