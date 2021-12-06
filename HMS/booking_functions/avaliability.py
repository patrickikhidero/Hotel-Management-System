import datetime
from HMS.models import Room, Booking

def check_avalaibility(room, check_in, check_out):
    avail_rooms = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_rooms.append(True)
        else:
            avail_rooms(False)
        return all(avail_rooms )