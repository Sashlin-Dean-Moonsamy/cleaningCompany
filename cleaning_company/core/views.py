from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

def index(request):
    return render(request, 'core/index.html')

def registerView(request):
    if request.POST:
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("base:dashboard")

    form = UserRegisterForm()
    return render(request, 'registration/register.html', {"form":form})
