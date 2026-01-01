from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("This is the Home page")


