from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from application.models import Setting as School, Testimonial
# Create your views here.


def home(request):
    return render(request, "home.html")


def school_settings(request):
    return {
        'school_settings': School.objects.first()
    }

def about(request):
    context = {
        'testimonials': Testimonial.objects.all()
    }
    return render(request, "about.html", context)


def contact(request):
    return render(request, "contact.html")


def programs(request):
    return render(request, "programs.html")

def program_detail(request, slug):
    context = {'slug': slug}
    return render(request, "program-detail.html", context)

