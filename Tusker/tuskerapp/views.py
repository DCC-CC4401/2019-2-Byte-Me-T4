from django.shortcuts import render

# Create your views here.
def userProfile(request):
    cssbootstrap = 'css/bootstrap.min.css'
    return render(request,'userProfile')