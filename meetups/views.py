from django.shortcuts import render

# Create your views here.

# index will take in the request parameter automatically by django.
def index(request):
    # return what you want to see when this views url is reached
    # render takes two arguments, request and the name of the template (path to template)
    return render(request, 'meetups/index.html')