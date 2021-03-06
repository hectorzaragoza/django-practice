from django.urls import path    
from . import views

# this is where we'll add the url patterns for this specific app
# path will take two arguments, first is the url endpoint and second is to specify the view funciton to be called when that url is reached
urlpatterns = [
    path('', views.index, name="all-meetups"), # our-domain.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_details, name="meetup-detail"),
] 
# connect this app to the global folder 