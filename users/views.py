from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')
