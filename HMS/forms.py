from django.contrib.auth import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user','email_verified',)

class UserDetail(DetailView):
    models = User
    template_name = 'user-dashboard-booking.html'
    context_object_name = 'user'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        # model = User
        # fields = ('price', 'user')
        fields = ('amount','email',)
        