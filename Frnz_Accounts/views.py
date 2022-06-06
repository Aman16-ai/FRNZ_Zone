import email
import re
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

def create_user(request):


    try:
        User.objects.get(username = request.POST.get('email').lower())
    except:
        pass
        if request.method=='POST':
            
            #create all fields to create user 
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            gender=request.POST['gender']

            # saving user to user models 
            user = User.objects.create_user(first_name = name, last_name = request.POST['gender'], username = request.POST.get('email').lower())
            user.set_password(request.POST.get('password'))
            user.save()
            return redirect('/')
        
        else:
            print("Bad request")


