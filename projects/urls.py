from django.contrib import admin
from django.urls import path
from projects import views

urlpatterns = [
    path('', views.home,name='home page'),
        path('about', views.home,name='home page'),
]
