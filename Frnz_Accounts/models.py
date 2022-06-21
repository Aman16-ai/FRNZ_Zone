import email
import datetime
from operator import le
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.
class Interset(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to ='expimg/',null=True,blank=True)
    fullname = models.CharField(max_length=200,null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    branch = models.CharField(max_length=20,null=True,blank=True)
    interests = models.ManyToManyField(Interset,null=True,blank=True)
    # synergy = models.CharField()
    want_synergy=models.BooleanField(blank=True, null=True)
    collage=models.CharField(max_length=200,blank=True, null=True)
    about = models.CharField(max_length=2000,blank=True, null=True)
    friends=models.ManyToManyField("self",related_name="friends")


    def __str__(self):
        return self.user.username
    
    
    @staticmethod
    def getUserProfileByUserId(user):
        userProfileobj = user_profile.objects.get(user = user)
        return userProfileobj
    
    @staticmethod
    def getUserProfileById(id):
        userProfileobj = user_profile.objects.get(pk = id)
        return userProfileobj
    
    @staticmethod
    def getUsersByCollege(college):
        users = user_profile.objects.filter(college = college)
        return users

    @staticmethod
    def getUsers(id):
        users = User.objects.get(id = id)
        return users

class Friend_request(models.Model):
    id = models.AutoField(primary_key=True)
    sender_user=models.ForeignKey(user_profile,on_delete=models.CASCADE,related_name="sender")
    receiver_user=models.ForeignKey(user_profile,on_delete=models.CASCADE,related_name="receiver")
    timestamp=models.DateField(default=datetime.datetime.now())
    status=models.BooleanField(default=False)

    @staticmethod
    def getReceiverFriendRequest(user):
        return Friend_request.objects.filter(receiver_user=user)

    @staticmethod
    def getAcceptedFriendRequest(user):
        return Friend_request.objects.filter(status=True)

    # def getPendingRequest():


    def __str__(self):
        return f'{self.sender_user.user.username} sends to {self.receiver_user.user.username} ({self.status})'

    



