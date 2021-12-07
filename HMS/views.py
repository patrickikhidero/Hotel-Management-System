from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import  login_required
import requests
from .models import * 
from . import forms
from .forms import CreateUserForm, CustomerForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.conf import settings

@login_required(login_url='login')
@admin_only
def receptionist(request):
    # def get(self, request, *args, **kwargs):
    return render(request, 'receptionist/index.html')

def homepage(request):
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    payment = Payment.objects.all()
    room_status = RoomStatus.objects.all()

    return render(request, 'index.html', {'rooms':rooms})

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def page_404(request):
    return render(request, 'page-404.html')

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            public_key = 'pk_test_16213e605869c12fef3c6c828d1361a4921412dd'
            return render(request, 'make_payment.html', {'payment': payment, 'paystack_public_key': public_key})
    else:
        payment_form = forms.PaymentForm()

    return render(request, 'initiate_payment.html', {'payment_form': payment_form})


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Successful Verifiction")
    else:
        messages.error(request, "Unable to verify your payment, please you balance.")
    return redirect('initiate-payment')


def payment_complete(request):
    return render(request, 'payment-complete.html')

def payment_received(request):
    return render(request, 'payment-received.html')

def room_details(request):
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    payment = Payment.objects.all()
    room_status = RoomStatus.objects.all()


    return render(request, 'room_details.html', {'rooms':rooms})


def room_grid(request):
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    # room_by_category = Room.objects.filter(category)
    payment = Payment.objects.all()
    room_status = RoomStatus.objects.all()
    data = {
        'rooms': rooms,
        # 'room_by_category': room_by_category
    }
    return render(request, 'room-grid.html', data)

# def customer_data(request, user_pk):
#     customer = Customer.objects.get(id=user_pk)

#     return render(request, 'user')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_dashboard_booking(request):
    bookings = Booking.objects.all()
    rooms = RoomStatus.objects.all()
    payment = Payment.objects.all()
    room_status = RoomStatus.objects.all()
    total_bookings = bookings.filter(user=request.user).count()
    total_pendings = room_status.filter(user=request.user, status='Pending').count()
    total_completed = room_status.filter(user=request.user, status='Expired').count()
    return render(request, 'user-dashboard-booking.html', {'bookings':bookings, 'rooms':rooms, 'payment':payment, 'total_bookings': total_bookings})


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_dashboard_profile(request):
    return render(request, 'user-dashboard-profile.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_dashboard_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'user-dashboard-settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_dashboard(request):
    bookings = Booking.objects.all()
    rooms = Room.objects.all()
    payment = Payment.objects.all()
    room_status = RoomStatus.objects.all()
    total_bookings = bookings.filter(user=request.user).count()
    
    total_pendings = room_status.filter(user=request.user,status='Pending').count()
    total_completed = room_status.filter(user=request.user,status='Expired').count()
    return render(request, 'user-dashboard.html', {'total_bookings': total_bookings, 'total_completed':total_completed, 'total_pendings':total_pendings})


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_profile(request):
    return render(request, 'user-profile.html')

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.info(request, 'Username and/or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

@unauthenticated_user
def registerPage(request):
   
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

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# class RoomList(ListView):
#     model=Room

# class BookingList(ListView):
#     model=Booking


        
