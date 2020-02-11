from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home),
    # path('rooms/', views.room),
    path('services/', views.service),
    path('aboutus/', views.about),
    path('blogs/', views.blog),
    path('b2/', views.b2),
    path('contacts/', views.contact),
    path('registration/', views.registration, name='registration'),
    path('signin/', views.login),
    path('blog1/', views.blog1),
    path('blog2/', views.blog2),
    path('blog3/', views.blog3),
    path('logout/', views.do_logout),
    path('reviews/', views.guestreviews),
    path('updatepage/', views.showupdatepage),
    path('saveupdate/<int:pk>', views.save_update),
    path('deletereview/<int:pk>', views.deleteReview),
    path('review/update/<int:pk>', views.updateReview),
    path('room/', include('usrs.urls'))


]
