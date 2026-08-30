from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("home page")

def about(request):
    return HttpResponse("about page")

def menu(request):
     return HttpResponse("menu page")

def booking(request):
    return HttpResponse("booking page")