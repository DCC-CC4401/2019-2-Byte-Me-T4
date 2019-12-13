from django.shortcuts import render

def userProfile(request):
    return render(request, 'userProfile.html')