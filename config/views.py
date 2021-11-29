from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

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

def payment_complete(request):
    return render(request, 'payment-complete.html')

def payment_received(request):
    return render(request, 'payment-received.html')

def room_details(request):
    return render(request, 'room-details.html')

def room_grid(request):
    return render(request, 'room-grid.html')

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

