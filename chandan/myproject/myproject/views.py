from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to Django")

def home_view(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse("This is about path")

