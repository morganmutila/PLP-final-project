from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def programs(request):
    return render(request, "programs.html")
