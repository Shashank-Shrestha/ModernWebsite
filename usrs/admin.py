from django.contrib import admin
from .models import Rooms, Bookings


# Register your models here.


class RoomDetails(admin.ModelAdmin):
    list_display = ('RoomType', 'Price', 'Facilities', 'Size', 'BedType', 'TotalRooms', 'image')


class UserBookings(admin.ModelAdmin):
    list_display = ('RoomType', 'Check_In', 'Check_Out', 'Adults', 'Children', 'BookedDate')


admin.site.register(Rooms, RoomDetails)
admin.site.register(Bookings, UserBookings)

