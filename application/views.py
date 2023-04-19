from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ApplicationForm
from django.views.generic import UpdateView

@login_required(login_url="login")
def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'application/success.html')
    else:
        form = ApplicationForm()
    return render(request, 'application/home.html', {'form': form})

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
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        # password2 = request.POST['password2']
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        user = authenticate(username = username, password=password1)
        login(request, user)
        messages.success(request, "Account created successfully, you can now apply")  
        return redirect("apply")
    
    else:
        return render(request, 'application/register.html')

def logoutUser(request):
    logout(request)
    return redirect('home')