from django.conf.urls import include
from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('chats',views.chat,name="chat"),
    path('register',views.register,name="register"),
    path('handleSignup',views.handleSignup,name="handleSignup"),
    path('login',views.login_page,name="login"),
    path('handelSignin',views.handlesignin,name="handelLogin"),
    path('logout',views.logout_view,name="handelLogin"),
    
]