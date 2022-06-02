import email
from operator import le
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.AutoField
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to ='expimg/')
    gender = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    intrests = models.CharField()
    # synergy = models.CharField()
    want_synergy=models.BooleanField()
    collage=models.CharField()
    about = models.CharField(max_length=2000)


    def __str__(self) -> str:
        return self.fullname
