from django.shortcuts import render

# Create your views here.

# index will take in the request parameter automatically by django.
def index(request):
    # return what you want to see when this views url is reached
    meetups = [
        { 
            'title': 'A First Meetup',
            'location': 'New York',
            'slug': 'a-first-meetup'
        },
        { 
            'title': 'A Second Meetup', 
            'location': 'Paris',
            'slug': 'a-second-meetup'
        }
    ]
    # render takes two arguments, request and the name of the template (path to template)
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })