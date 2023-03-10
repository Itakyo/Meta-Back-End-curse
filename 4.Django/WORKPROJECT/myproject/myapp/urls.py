##ESTA PAGIAN ESTABA VACIA TOCO DESDE CERO 
from django.urls import path, include
#from myapp import views
from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('menu/', views.menu, name="menu"),
        path('about/', views.about, name="about"),
        path('book/', views.book, name="book"),
] 

# urlpatterns = [
#     path('dishes/<str:dish>', views.menuitems   ) #dish=pasta,
# ]

# urlpatterns = [
#     path('home/', views.home),
# ]