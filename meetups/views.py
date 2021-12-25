from django.shortcuts import render, redirect

from meetups.forms import RegistrationForm
from .models import Meetup, Participant
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
        if request.method == 'GET':
            registration_form = RegistrationForm() 
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)


        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        print('This is the exc: ', exc)
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {'organizer_email': meetup.organizer_email})