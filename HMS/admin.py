from django.contrib import admin
from .models import *
# Register your models here.
 

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(RoomStatus)
admin.site.register(Payment)