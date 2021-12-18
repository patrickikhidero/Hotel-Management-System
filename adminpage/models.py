from django.db import models
import uuid 
# import os 
# import psycopg2 
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from django.forms.utils import to_current_timezone
from django.utils.timezone import  datetime
import secrets

# Create your models here.

class Admins(models.Model) : 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=200) 
    last_name = models.CharField(null=True, max_length=200) 
    email = models.EmailField(null=True, unique=True) 
    username = models.CharField(null=True, max_length=100) 
    email_verified = models.BooleanField(null=True, unique=True) 
    phone_number = models.CharField(null=True, max_length=100, unique=True) 
    profile_pic = models.ImageField(default='avataruser.png', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self) : 
        return f'{self.user}' 