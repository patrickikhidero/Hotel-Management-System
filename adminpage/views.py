from django.shortcuts import render
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import  User
import requests
from .models import * 
from HMS.models import * 
from . import forms
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.conf import settings

# Create your views here.
@unauthenticated_user
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminhome')
        else:
            messages.info(request, 'Username and/or Password is incorrect')

    context = {}
    return render(request, 'receptionist/templates/adminlogin.html', context)



def adminregister(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            
            # Customer.objects.create(
            #     user=user,
            #     name = user.username,
            # )

            messages.success(request, 'Registrations Successful for ' + username)

            return redirect('adminlogin')

    context = {'form': form}

    return render(request, 'receptionist/templates/adminregister.html', context)

def logoutPage(request):
    logout(request)
    return redirect('adminlogin')




@login_required(login_url='adminlogin')
@admin_only
# @allowed_users(allowed_roles=['admin', 'receptionist', 'managerrole'])
def adminhome(request):
    users = User.objects.all()
    customers = Customer.objects.all()
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    payment = Payment.objects.all()
    room_status = RoomStatus.objects.all()
    total_bookings = bookings.filter().count()
    total_customer = customers.filter().count()
    total_pendings = room_status.filter(status='Pending').count()
    total_available = room_status.filter(status='Expired').count()
    # total_availble_rooms = room_status.filter(status='').count()
    return render(request, 'receptionist/templates/index.html', {'total_customer': total_customer, 'payment': payment, 'bookings': bookings, 'rooms': rooms,  'total_bookings': total_bookings, 'total_available':total_available, 'total_pendings':total_pendings})

def add_asset(request):
    return render(request, 'receptionist/templates/add-asset.html')

def add_booking(request):
    return render(request, 'receptionist/templates/add-booking.html')

def add_customer(request):
    return render(request, 'receptionist/templates/add-customer.html')

def add_employee(request):
    return render(request, 'receptionist/templates/add-employee.html')

def add_room(request):
    return render(request, 'receptionist/templates/add-room.html')

def add_role(request):
    return render(request, 'receptionist/templates/add-room.html')

def add_staff(request):
    return render(request, 'receptionist/templates/add-staff.html')

def add_salary(request):
    return render(request, 'receptionist/templates/add-salary.html')



def edit_asset(request):
    return render(request, 'receptionist/templates/edit-asset.html')

def edit_booking(request):
    return render(request, 'receptionist/templates/edit-booking.html')

def edit_customer(request):
    return render(request, 'receptionist/templates/edit-customer.html')

def edit_employee(request):
    return render(request, 'receptionist/templates/edit-employee.html')

def edit_room(request):
    return render(request, 'receptionist/templates/edit-room.html')

def edit_staff(request):
    return render(request, 'receptionist/templates/edit-staff.html')

def edit_salary(request):
    return render(request, 'receptionist/templates/edit-salary.html')

