from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.

def index(request):
    context1 = {
        "variable1": "this is variable 1!"
    }
    return render(request, 'index.html', context1)
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, 'About.html')
    # return HttpResponse('this is about page')


def services(request):
    return render(request, 'Services.html')
    # return HttpResponse('this is service page')

def aiml(request):
    return render(request, 'aiml.html')

def automation(request):
    return render(request, 'automation.html')

def cloud(request):
    return render(request, 'cloud.html')

def Iot(request):
    return render(request, 'Iot.html')

def Other(request):
    return render(request, 'Other.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        country = request.POST.get("country")
        service = request.POST.get("service")
        text = request.POST.get("text")
        contact = Contact(name=name, email = email, phone=phone, country=country, service=service,
                          text=text)
        contact.save()
        messages.success(request, 'Submitted successfully, will get back to you soon!')

    return render(request, 'Contact.html')
    # return HttpResponse('this is a contact page')
