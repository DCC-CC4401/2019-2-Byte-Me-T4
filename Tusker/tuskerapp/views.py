from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from .forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def userProfile(request):
    return render(request, 'userProfile')

def landingPage(request):
    return render(request, 'landingPage')

def index(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            form = SignInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=raw_password)
                if user is None:
                    messages.error(request, 'email or password not correct')
                else:
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/landingPage')
        elif request.POST.get('submit') == 'sign_up':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                #email = form.cleaned_data.get('email')
                #raw_password = form.cleaned_data.get('password')
                #user = authenticate(email=email, password=raw_password)
                login(request, user)
                return redirect('http://127.0.0.1:8000/landingPage')
    signin_form = SignInForm()
    signup_form = SignUpForm()
    return render(request, 'index', context={"upform": signup_form, "inform": signin_form})
