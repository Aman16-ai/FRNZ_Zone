import email
import re
from tkinter import E
from urllib.request import HTTPRedirectHandler
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

# Create your views here.

def home(request):
    return render(request,"index.html")

def chat(request):
    return render(request,"chat.html")

def register(request):
    return render(request,"register.html")

def handleSignup(request):

        if request.method == 'POST':
            print("called")
            username = request.POST['Username']
            firstname = request.POST['Firstname']
            lastname = request.POST['Lastname']
            email = request.POST['Email']
            password = request.POST['Password']
            
            try :
                user = User.objects.create_user(username=username,email=email,password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                return redirect("/")
            except:
                return HttpResponse("Registration failed")
        return HttpResponse("Something went wrong")


