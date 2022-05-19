from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("aiml", views.aiml, name='AIML'),
    path("automation", views.automation, name='Auto'),
    path("Other", views.Other, name='Other'),
    path("cloud", views.cloud, name='Cloud'),
    path("Iot", views.Iot, name='Iot'),

]
