from django.conf.urls import include
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home),
    path('chats',views.chat),
    path('register',views.register)
    
]