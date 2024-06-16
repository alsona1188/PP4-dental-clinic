from django.shortcuts import render
from django.views import generic
from .models import Service, Dentist

# Create your views here.

def home(request):
    # Retrieve all services and dentists from the database
    services = Service.objects.all()
    dentists = Dentist.objects.all()
    
    # Pass the data to the template
    return render(request, 'home.html', {'services': services, 'dentists': dentists})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services,})




   
