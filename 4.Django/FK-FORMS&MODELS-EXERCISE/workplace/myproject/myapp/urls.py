from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('home/', views.form_view)
]