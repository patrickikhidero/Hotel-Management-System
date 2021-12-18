from django.contrib.auth import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from HMS.models import * 
from .models import *


class AdminForm(ModelForm):
    class Meta:
        model = Admins
        fields = '__all__'
        exclude = ('user','email_verified',)

class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class BookingForm(ModelForm):
    class Meta:
        models = Booking
        fields = '__all__'
        # context_object_name = 'booking'
        