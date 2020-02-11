from django.contrib import admin
from .models import Booking, Review


# Register your models here.


class AdminBooking(admin.ModelAdmin):
    list_type = ('RoomType', 'Check_In', 'Check_Out', 'Adults', 'Children')


admin.site.register(Booking, AdminBooking)


