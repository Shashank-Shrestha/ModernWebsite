from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.utils.timezone import now


class Rooms(models.Model):
    RoomType = models.CharField(max_length=100)
    Price = models.FloatField()
    Facilities = models.TextField()
    Size = models.IntegerField()
    BedType = models.CharField(max_length=100)
    TotalRooms = models.IntegerField(default=0)
    image = models.FileField()

    def __str__(self):
        return str(Rooms.RoomType)


class Bookings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    RoomType = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    Check_In = models.TextField()
    Check_Out = models.TextField()
    Adults = models.IntegerField(null='True')
    Children = models.IntegerField(null='True')
    BookedDate = models.DateField(default=now)








