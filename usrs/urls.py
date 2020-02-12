from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room),
    path('booklist/', views.bookings),
    path('book/', views.mybooking),
    path('loginfirst', views.login_first),
     path('cancel/<int:pk>/', views.cancelroom),



]
