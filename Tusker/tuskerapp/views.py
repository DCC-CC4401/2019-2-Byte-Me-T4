from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
        text = "<h1>EXITOOO</h1>"
        return HttpResponse(text)
