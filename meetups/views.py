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


def meetup_details(request):
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
        }
    return render(request, 'meetups/meetup-detials.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']})