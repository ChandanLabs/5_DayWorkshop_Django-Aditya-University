from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.home, name='home'),
    path("home/",views.home_view, name='home_view'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("services",views.services, name='services'),
    path("register/", views.register, name='register'),
    path("details/", views.details, name='details'),
    path("update/<int:id>/", views.update, name='update'),
    path("delete/<int:id>/", views.delete, name='delete'),
]
