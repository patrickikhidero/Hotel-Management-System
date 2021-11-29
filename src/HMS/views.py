from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import  login_required




def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def page_404(request):
    return render(request, 'page-404.html', {})

def payment_complete(request):
    return render(request, 'payment-complete.html', {})

def payment_received(request):
    return render(request, 'payment-received.html', {})

def room_details(request):
    return render(request, 'room-details.html', {})

def room_grid(request):
    return render(request, 'room-grid.html', {})

def user_dashboard_booking(request):
    return render(request, 'user-dashboard-booking.html')

def user_dashboard_profile(request):
    return render(request, 'user-dashboard-profile.html')

def user_dashboard_reviews(request):
    return render(request, 'user-dashboard-reviews.html')

def user_dashboard_wishlist(request):
    return render(request, 'user-dashboard-wishlist.html')

def user_dashboard(request):
    return render(request, 'user-dashboard.html')

def user_profile(request):
    return render(request, 'user-profile.html')
       
def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.get(email=email).exists():
                messages.error(request, 'User already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email = email, first_name=firstname, last_name=lastname)
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                user.save()
                return redirect('dashboard')
        else:
            messages.error(request, 'Password does not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboad')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

# @login_required(login_url='signin')
# def dashboard(request):
#     blogs = Post.objects.order_by('-created_on').filter(author_id=request.user.id)
#     data = {
#         'hotel': config,
#     }
#     return render(request, 'dashboard.html', data)




        
