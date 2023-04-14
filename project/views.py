from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from application.models import Setting as School, Testimonial, Program, StudyCategory
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    programs = Program.objects.all()
    no_of_programs = programs.count()
    no_of_studnets = User.objects.filter(is_staff=0).count()

    context = {
        'programs' : programs,
        'no_of_programs' : no_of_programs,
        'no_of_students' : no_of_studnets,
        'no_of_levels': StudyCategory.objects.all().count(),

    }
    return render(request, "home.html", context)



def about(request):

    context = {
        'no_of_programs' : Program.objects.all().count(),
        'no_of_students' : User.objects.filter(is_staff=0).count(),
        'testimonials': Testimonial.objects.all(),
        'no_of_levels': StudyCategory.objects.all().count(),
    }
    
    return render(request, "about.html", context)


def contact(request):
    return render(request, "contact.html")


def programs(request):
    programs = Program.objects.all()
    context = {
        'programs' : programs,
    }
    return render(request, "programs.html", context)

def program_detail(request, slug):
    program_detail = get_object_or_404(Program, slug = slug) 
    context = {'program': program_detail}
    return render(request, "program-detail.html", context)

