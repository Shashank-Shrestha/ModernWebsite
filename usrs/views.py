from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Rooms, Bookings


def room(request):
    if request.method == 'POST':
        key = request.POST['key']
        rooms = Rooms.objects.filter(Q(RoomType__icontains=key))
        return render(request, "rooms.html", {'room': rooms})

    rooms = Rooms.objects.all()
    return render(request, "rooms.html", {'room': rooms})


def bookings(request):
    if request.method=="POST":
        rid=request.POST['id']
        obj=Bookings.objects.get(id=rid)
        obj.RoomType.RoomType=request.POST['roomtype']
        obj.RoomType.Price=request.POST['mid']
        obj.Check_In=request.POST['checkin']
        obj.Check_Out=request.POST['checkout']
        obj.Adults=request.POST['adult']
        obj.Children=request.POST['child']
        obj.save()
    booking = Bookings.objects.filter(user_id=request.user)
    return render(request, "mybooking.html", {'booking': booking})

def mybooking(request):

    if request.method == 'POST':
        room_type = request.POST.get('roomtype')
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        adults = request.POST.get('adult')
        children = request.POST.get('child')
        fk_room = Rooms.objects.get(RoomType=room_type)
        fk_user = request.user.id
        print(room_type)
        print(check_in)
        print(check_out)
        print(adults)
        print(children)
        book = Bookings(RoomType=fk_room, Check_In=check_in, Check_Out=check_out,
                                      Adults=adults, Children=children, user_id=fk_user)
        book.save()
        current_user = request.user
        messages.info(request, 'INFO: You are Booking is successfully done, To check your bookings Please goto Mybooking')
        return render(request, 'rooms.html', {'current_user': current_user})


def cancelroom(request, pk):
    canceled = Bookings.objects.get(id=pk)
    canceled.delete()
    return redirect('../../../bookings/booklist')


def login_first(request):
    return render(request, 'login.html')


