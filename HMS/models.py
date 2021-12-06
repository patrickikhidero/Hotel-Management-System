from django.db import models 
import uuid 
# import os 
# import psycopg2 
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from django.forms.utils import to_current_timezone
from django.utils.timezone import  datetime

# class UserProfile(AbstractUser): 
#     first_name = models.CharField(max_length=50, blank=True, null=True) 
#     last_name = models.CharField(max_length=50, blank=True, null=True) 
#     phone_number = models.CharField(max_length=100,blank=True, null=True) 
#     avatar_url = models.URLField(blank=True, null=True) 
#     otp_code = models.CharField(max_length=100,blank=True, null=True) 
#     gender = models.CharField(max_length=7, blank=True, null=True) 
    
#     def __str__(self): 
#         return f'{self.first_name}' 
        

class Receptionist(models.Model): 
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    user_id = models.UUIDField(unique=True) 
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    gender = models.CharField(max_length=7) 
    avartar_url = models.CharField(default=None, max_length=200, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    
    def __str__(self): 
        return f'{self.first_name} {self.last_name} is a {self.gender} receptions' 
        
        
class Room(models.Model): 
    room_types = [ 
        ('All Rooms', 'All Rooms'),
        ('Dorm Beds', 'Dorm Beds'), 
        ('Private Room', 'Private Room'), 
        ('Suites', 'Suites'),
    ]
    numbers = models.IntegerField(default = 0,)
    category = models.CharField(max_length=24, default = 0, choices=room_types) 
    beds = models.IntegerField(default=0)
    capacity =  models.IntegerField(default=0)


    # id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    # type = models.CharField(max_length=100, choices=types) 
    # price = models.CharField(max_length=100) 
    # created_at = models.DateTimeField(auto_now_add=True, null=True) 
    # updated_at = models.DateTimeField(auto_now=True) 
        
    def __str__(self): 
        return f'{self.numbers}. {self.category} with {self.beds} for {self.capacity} people' 


class Booking(models.Model):
     user = models.ForeignKey(User, default = 0, on_delete=models.CASCADE)
     room = models.ForeignKey(Room, default = 0, on_delete=CASCADE)
     check_in = models.DateTimeField(default = datetime.now, blank = True)
     check_out = models.DateTimeField(default = datetime.now, blank = True)

     def __str__(self):
         return f'{self.user}. has booked{self.room} from {self.check_in} to {self.check_out}'
    
        
class RoomStatus(models.Model) : 
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    status = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self) : 
        return self.status 


# class RoomType(models.Model) : 
#     id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
#     room_type_id = models.ForeignKey(Room, on_delete=models.CASCADE) 
#     room_no = models.CharField(max_length=50) 
#     location = models.CharField(max_length=200) 
#     description = models.TextField(null=True) 
#     single_room_img = models.TextField(null = True) 
#     single_room_img2 = models.TextField(null=True) 
#     img_url = models.TextField(null=True) 
#     room_status_id = models.ForeignKey(RoomStatus, on_delete=models.CASCADE) 
#     price = models.CharField(max_length=100) 
#     booked = models.BooleanField(default=False) 
#     created_at = models.DateTimeField(auto_now_add=True) 
#     updated_at = models.DateTimeField(auto_now=True) 
    
#     def __str__(self) : 
#         return f'{self.room_type_id}' 
        
        
class Customer(models.Model) : 
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=200) 
    last_name = models.CharField(null=True, max_length=200) 
    email = models.EmailField(null=True, unique=True) 
    username = models.CharField(null=True, max_length=100) 
    email_verified = models.BooleanField(null=True, unique=True) 
    phone_number = models.CharField(null=True, max_length=100, unique=True) 
    profile_pic = models.ImageField(default='avataruser.png', null=True, blank=True)
    next_of_kin_fullname = models.CharField(null=True, max_length=100) 
    next_of_kin_phone_number = models.CharField(null=True, max_length=100, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self) : 
        return f'{self.user}' 


class PaymentType(models.Model) : 
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self) : 
        return self.name 
        
class Bookings(models.Model) : 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, null=True) 
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE, null=True) 
    payment_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE, null=True) 
    start_time = models.DateField(blank=True, null=True) 
    end_time = models.DateField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    

class Payment(models.Model) : 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE) 
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    payment_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 


class Reservation(models.Model) : 
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE) 
    payment_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE) 
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE) 
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True)