from django.db import models 
import uuid 
# import os 
# import psycopg2 
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from django.forms.utils import to_current_timezone
from django.utils.timezone import  datetime
import secrets
from .paystack import PayStack

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
    amount =  models.IntegerField(default=0)
  
    def __str__(self): 
        return f'{self.category} with {self.beds}bed(s), and {self.capacity} occupant(s). Cost is {self.amount}' 

class Payment(models.Model) : 
    # user = models.ForeignKey(User, default = 0, on_delete=models.CASCADE)
    # room = models.ForeignKey(Room, default = 0, on_delete=CASCADE)
    email = models.EmailField(null=True)
    ref = models.CharField(max_length=200, null=True)
    amount = models.PositiveIntegerField(null=True) 
    verified = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    class Meta:
        ordering = ('-created_at',)
    def __str__(self) -> str : 
        return f"Payment: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
    
    def amount_value(self) -> int:
        return self.amount * 100
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False


class RoomStatus(models.Model) : 
    room_status = [ 
        ('Pending', 'Pending'),
        ('Paid', 'Paid'), 
        ('Expired', 'Expired'), 
    ]
    user = models.ForeignKey(User, default = 0, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, default = 0, on_delete=CASCADE)
    status = models.CharField(max_length=20, default = 0, choices=room_status)
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self) : 
        return f'{self.room} is currently {self.status}'

class Booking(models.Model):
    user = models.ForeignKey(User, default = 0, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, default = 0, on_delete=CASCADE)
    location = models.CharField(null=True, max_length=100) 
    check_in = models.DateTimeField(default = datetime.now, blank = True)
    check_out = models.DateTimeField(default = datetime.now, blank = True)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True) 
    status = models.ForeignKey(RoomStatus, on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return f'{self.user} has booked {self.room} located at {self.location}'
    
        



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

        
class Bookings(models.Model) : 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, null=True) 
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE, null=True) 
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True) 
    start_time = models.DateField(blank=True, null=True) 
    end_time = models.DateField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.CharField(null=True, max_length=20) 
    

class Reservation(models.Model) : 
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE) 
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE) 
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE) 
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True, null=True) 
    updated_at = models.DateTimeField(auto_now=True)