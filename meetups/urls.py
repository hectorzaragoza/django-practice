from django.urls import path    
from . import views
# this is where we'll add the url patterns for this specific app
# path will take two arguments, first is the url endpoint and second is to specify the view funciton to be called when that url is reached
urlpatterns = [
    path('meetups', views.index) # our-domain.com/meetups
]

# connect this app to the global folder 