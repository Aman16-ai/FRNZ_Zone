from cmath import rect
from ctypes import sizeof
import email
from itertools import count
import re
from tkinter import E
from traceback import print_tb
from urllib.request import HTTPRedirectHandler
from django.dispatch import receiver
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .models import Friend_request, user_profile
# Create your views here.

def home(request):
    # if request.user.is_authenticated:
    #     return render(request,"chat2.html")
    # else:
        return render(request,"index.html")

@login_required(login_url='/login')
def chat(request):
    return render(request,"chat.html")

def register(request):
    return render(request,"register1.html")

def login_page(request):
    return render(request,"signin.html")

def handleSignup(request):

        if request.method == 'POST':
            username = request.POST['Username']
            firstname = request.POST['Firstname']
            lastname = request.POST['Lastname']
            email = request.POST['Email']
            password = request.POST['Password']
            
            try :
                user = User.objects.create_user(username=username,email=email,password=password)
                user.first_name = firstname
                user.last_name = lastname
                if user is not None:
                    userProfile = user_profile(user = user,fullname = firstname+" "+lastname)
                    userProfile.save()
                    user.save()
                    return redirect("/")
                else:
                    return HttpResponse("user not created")
            except:
                return HttpResponse("Registration failed")
        return HttpResponse("Something went wrong")


def handlesignin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))
        if user is not None :
            login(request, user)
            print(user)
            return redirect('/')
        else:
            return HttpResponse("Something went wrong")

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login')
def edit_profile(request):
    # Fetching authenticated user1 
    user1=user_profile.getUserProfileByUserId(request.user)
    get_user=User.objects.get(username__contains=request.user)
    print(user1.user.email)

    # Total friends objects ( wheter True or False )
    friend_req=Friend_request.getReceiverFriendRequest(user1)

    # For total friends ( Accepted )
    total_friends=user1.friends.all()
    # print(total_friends)

    # For total friend request pending ( Currently false )
    friendlist=[]
    for i in friend_req:
        if(i.status==False):
            friendlist.append(i)

    param={ 'data':user1,
            'user':get_user,
            'friendscount':len(friendlist),
            'friends_req':friendlist,
            'total_friends':len(total_friends)}

    return render(request,"edit_profile.html",param)

@login_required(login_url='/login')
def acceptreq(request,senderid):
    receiveruser=user_profile.getUserProfileByUserId(request.user)
    senderuser=user_profile.getUserProfileById(senderid)
    receiveruser.friends.add(senderuser)
    friendreq=Friend_request.getReceiverFriendRequest(receiveruser)
    print(friendreq)
    for friend in friendreq:
        if friend.sender_user == senderuser:
            # print(friend.sender_user)
            friend.status=True
            # friend.delete()
            friend.save()
    return redirect('/editprofile')

@login_required(login_url='/login')
def declinereq(request,senderid):
    receiveruser=user_profile.getUserProfileByUserId(request.user)
    senderuser=user_profile.getUserProfileById(senderid)
    friendreq=Friend_request.getReceiverFriendRequest(receiveruser)
    for friend in friendreq:
        if friend.sender_user == senderuser:
            # print(friend.sender_user)
            print(friend.sender_user)
            friend.delete()
    print(friend)
    return redirect('/editprofile')

    

