from datetime import datetime

from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Booking, Review, Contactus
from django.contrib.auth.models import User
# from hotel_booking.usrs.models import Rooms
# Create your views here.


def home(request):
    # if request.method == 'POST':
    #     room_type = request.POST.get('roomtype')
    #     check_in = request.POST.get('checkin')
    #     check_out = request.POST.get('checkout')
    #     adults = request.POST.get('adult')
    #     children = request.POST.get('child')
    #     print(room_type)
    #     print(check_in)
    #     print(check_out)
    #     print(adults)
    #     print(children)
    #     book = Booking.objects.create(RoomType=room_type, Check_In=check_in, Check_Out=check_out,
    #                                   Adults=adults, Children=children)
    #     book.save()
    #     return render(request, 'index.html')
    return render(request, 'index.html')
    # return render(request,"home.html")


def service(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def b2(request):
    return render(request, "b2.html")


def contact(request):
    current_user = request.user.id
    # logged_in_user = User.objects.get(id=current_user)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        messages = request.POST['message']
        contactss = Contactus(Name=name,Email=email,Messages=messages)
        contactss.save()

    return render(request, "contact.html")


def registration(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        usernames = request.POST.get('username')
        passwords = request.POST.get('password')
        confirm_password = request.POST.get('passwordConfirmation')
        if passwords == confirm_password:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=usernames,
                                            password=passwords)
            user.save()
            messages.info(request, 'INFO: You are successfully registered,Please goto SignIn to Login')
            # return HttpResponse('<script>alert("You are Registered successfully, Please go to Login page.") </script>')

    return render(request, "registration.html")


def login(request):
    email = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == 'POST':
        usr = auth.authenticate(username=email, password=password)

        if usr is not None:
            auth.login(request, usr)
            return redirect('/home')
        else:
            messages.error(request, 'Error: Username or Password is incorrect')
    return render(request, "login.html")


# def login(request):
#     if 'email' not in request.session:
#         return render(request, 'login.html')
#     else:
#         return redirect('index.html')


def blog1(request):
    return render(request, "blog1.html")


def blog2(request):
    return render(request, "blog2.html")


def blog3(request):
    return render(request, "blog3.html")


def do_logout(request):
    auth.logout(request)
    return redirect('../home')


def guestreviews(request):
    review = Review.objects.all()
    if request.method == "POST":
        current_user = request.user
        user_review = request.POST.get('user_review')
        user_date = datetime.now()
        review = Review(user=current_user, message=user_review, date=user_date)
        review.save()
        return redirect('/reviews')
    return render(request, "guestreview.html", {'review': review})


# def myBooking(request):
#     bookings = Booking.objects.all()
#     return render(request, "mybooking.html", {'bookings': bookings})


def deleteReview(request, pk):
    del_review = Review.objects.get(id=pk)
    del_review.delete()
    return redirect('/reviews')


def updateReview(request, pk):
    update_review = Review.objects.get(id=pk)
    return render(request, "update.html", {'update': update_review})


def showupdatepage(request):
    return render(request, "update.html")


def save_update(request,pk):

    if request.method == 'POST':
        review = Review.objects.get(id=pk)
        review_message = request.POST.get('user_review')
        review.message = review_message
        review.user = request.user
        # Review(message=review_message, user=request.user)
        review.save()

    return redirect('/reviews')









