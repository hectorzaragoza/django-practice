from django.shortcuts import render
from .models import Meetup

# Create your views here.

# index will take in the request parameter automatically by django.
def index(request):
    # return what you want to see when this views url is reached
    # THis is dummy data for initial testing
    # meetups = [
    #     { 
    #         'title': 'A First Meetup',
    #         'location': 'New York',
    #         'slug': 'a-first-meetup'
    #     },
    #     { 
    #         'title': 'A Second Meetup', 
    #         'location': 'Paris',
    #         'slug': 'a-second-meetup'
    #     }
    # ]
    # This is the real, database run data display
    meetups = Meetup.objects.all()

    # render takes two arguments, request and the name of the template (path to template)
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description})
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })