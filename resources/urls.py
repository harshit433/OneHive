from django.contrib import admin
from django.urls import path
from resources import views

urlpatterns = [
    path('', views.home,name='home page'),
        path('about', views.home,name='home page'),
]
