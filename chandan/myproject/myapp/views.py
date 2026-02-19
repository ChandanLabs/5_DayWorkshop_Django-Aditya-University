from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Info

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        salary = request.POST['salary']
        email = request.POST['email']
        info = Info(name=name, age=age, salary=salary, email=email)
    return render (request, 'home.html')

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

def services(request):
    return HttpResponse("This is services page")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        salary = request.POST.get('salary', '')
        email = request.POST.get('email', '')
        


    info = Info(name=name, age=age, salary=salary, email=email)
    return render(request, 'register.html')

def details(request):
    infos = Info.objects.all()
    return render(request, 'details.html', {'infos': infos})
    
