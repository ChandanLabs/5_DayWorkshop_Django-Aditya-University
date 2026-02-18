from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Info

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Myapp")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

def services(request):
    return HttpResponse("This is services page")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        salary = request.POST.get('salary', '').strip()
        email = request.POST.get('email', '').strip()
        


    
    return render(request, 'register.html')

def details(request):
    infos = Info.objects.all()
    return render(request, 'details.html', {'infos': infos})
    
