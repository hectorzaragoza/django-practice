from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# index will take in the request parameter automatically by django.
def index():
    # return what you want to see when this views url is reached
    return HttpResponse('Hello World')