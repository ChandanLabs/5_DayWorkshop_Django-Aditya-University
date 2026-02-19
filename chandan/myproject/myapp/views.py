from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Info

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Home page")

def home_view(request):
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
        
        # Create and save the Info object (CREATE operation)
        info = Info(name=name, age=age, salary=salary, email=email)
        info.save()
        
        messages.success(request, 'Registration successful!')
        return redirect('register')
    
    return render(request, 'register.html')

def details(request):
    infos = Info.objects.all()
    return render(request, 'details.html', {'infos': infos})

# UPDATE operation - Edit existing record
def update(request, id):
    info = Info.objects.get(id=id)
    
    if request.method == 'POST':
        info.name = request.POST.get('name')
        info.age = request.POST.get('age')
        info.salary = request.POST.get('salary')
        info.email = request.POST.get('email')
        info.save()
        messages.success(request, 'Update successful!')
        return redirect('details')
    
    return render(request, 'update.html', {'info': info})

# DELETE operation - Delete existing record
def delete(request, id):
    info = Info.objects.get(id=id)
    info.delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('details')
    
