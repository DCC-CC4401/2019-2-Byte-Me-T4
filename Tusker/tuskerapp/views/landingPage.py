from django.shortcuts import render

def landingPage(request):
    return render(request, 'userProfile.html')