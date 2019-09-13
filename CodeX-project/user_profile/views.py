from django.shortcuts import render


def home(request):
    return render(request, 'user_profile/home.html')


def register(request):
    return render(request, 'user_profile/register.html')


def login(request):
    return render(request, 'user_profile/login.html')