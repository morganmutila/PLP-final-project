from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, forms
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# @login_required(login_url='application.login')
def home(request):
    context = {
        'is_apply' : request.path.startswith('/application'),
        'page' : request.path
    }

    return render(request, "application/home.html", context)

def loginView(request):
    if request.user.is_authenticated:
        return redirect('apply')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('apply')
        else:
            messages.error(request, "Username or password does not exist")


    context = {}

    return render(request, 'application/login.html', context)

def registerView(request):
    if request.user.is_authenticated:
        return redirect('apply')

    if request.method == 'POST':  
        form = UserCreationForm(request.POST)      
        if form.is_valid():  
            user = form.save() 
            # email = form.cleaned_data.get('email').lower()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email = email, password=raw_password)
            # login(request, user)
            messages.success(request, f'Account for {{ user.name }} created successfully, You can now log in')  
            return redirect("apply")
    else: 
        form = UserCreationForm()

    context = {
        'form' : form,
    }
    
    return render(request, 'application/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')