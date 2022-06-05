import email
from operator import le
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Interset(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class user_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=0)
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to ='expimg/',null=True,blank=True)
    gender = models.CharField(max_length=10)
    branch = models.CharField(max_length=20,null=True,blank=True)
    interests = models.ManyToManyField(Interset)
    # synergy = models.CharField()
    want_synergy=models.BooleanField()
    collage=models.CharField(max_length=200)
    about = models.CharField(max_length=2000)


    def __str__(self):
        return self.fullname


