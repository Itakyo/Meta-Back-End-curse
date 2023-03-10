from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.
def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", {'content': about_content})

# def menu(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
#     menuitems = {'mains': [
#         {'name':"falafael", 'price':"12"},
#         {'name':"Pasta", 'price':"16"},
#         {'name':"Chino", 'price':"17"},
#         {'name':"Merenge", 'price':"14"}
#     ]}
#     return render(request, "menu.html", {'content': about_content})

# def menu(request):
    
#     menuitems = {'mains': [
#         {'name':"falafael", 'price':"12"},
#         {'name':"Pasta", 'price':"16"},
#         {'name':"Chino", 'price':"17"},
#         {'name':"Merenge", 'price':"14"}
#     ]}
#     return render(request, 'menu.html', menuitems)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)