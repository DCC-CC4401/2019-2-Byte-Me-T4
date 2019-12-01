import logging
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def userProfile(request):
    return render(request, 'userProfile')

def landingPage(request):
    return render(request, 'landingPage')

def index(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            form = UserCreationForm(request.POST)
            #if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            #logging.info(email)
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('userProfile')
        elif request.POST.get('submit') == 'sign_up':
            return
    else:
        return render(request, 'index')
