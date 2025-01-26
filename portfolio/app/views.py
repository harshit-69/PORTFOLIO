
from django.shortcuts import render
from app.models import contacts

from datetime import datetime

def home(request):
    return render(request,"home.html")

def flask(request):
    return render(request, "flask.html")

def nlp(request):
    return render(request, "nlp.html")

def ml(request):
    return render(request,"ml.html")


def bi(request):
    return render(request,"bi.html")

def about(request):
    return render(request,"about.html")

def certificate(request):
    return render(request,"certificate.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        contact=contacts(name=name,email=email,phone=phone,message=message,date=datetime.today())
        contact.save()

    return render(request,"contact.html")



