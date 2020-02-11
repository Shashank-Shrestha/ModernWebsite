from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# from hotel_booking.usrs.models import Rooms


class Booking(models.Model):
    #RoomType = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    RoomType = models.CharField(max_length=100)
    Check_In = models.TextField()
    Check_Out = models.TextField()
    Adults = models.IntegerField(null='True')
    Children = models.IntegerField(null='True')


# class Room_cost(models.Model):
#     RoomType = models.TextField()
#     Price = models.FloatField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField(default=now)


class Contactus(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Messages = models.TextField()









