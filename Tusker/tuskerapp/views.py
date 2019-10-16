from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def userProfile(request):
    cssbootstrap = 'css/bootstrap.min.css'
    return render(request, 'userProfile')

def landingPage(request):
    cssbootstrap = 'css/bootstrap.min.css'
    return render(request, 'landingPage')