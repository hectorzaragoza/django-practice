from django.urls import path    
from . import views
from django.conf.urls.static import static
from django.conf import settings
# this is where we'll add the url patterns for this specific app
# path will take two arguments, first is the url endpoint and second is to specify the view funciton to be called when that url is reached
urlpatterns = [
    path('meetups/', views.index, name="all-meetups"), # our-domain.com/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_details, name="meetup-detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# connect this app to the global folder 