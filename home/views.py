from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse('This is home page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('This is about page')

def services(request):
    return render(request, 'services.html')
    return HttpResponse('This is services page')

def contact(request):
    if request.method == "post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('msg')
        contact = Contact(name=name, email=email, phone=phone, desc=msg, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
    return HttpResponse('This is contact page')