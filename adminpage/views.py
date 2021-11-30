from django.shortcuts import render

# Create your views here.
def adminhome(request):
    return render(request, 'receptionist/templates/index.html')

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

