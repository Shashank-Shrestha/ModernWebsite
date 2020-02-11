import os
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# class Booking(models.Model):
#     RoomType = models.CharField(max_length=100)(on_delete=models.CASCADE)
#     Check_In = models.TextField()
#     Check_Out = models.TextField()
#     Adults = models.IntegerField(null='True')
#     Children = models.IntegerField(null='True')


class Room_cost(models.Model):
    RoomType = models.TextField()
    Price = models.FloatField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(now)