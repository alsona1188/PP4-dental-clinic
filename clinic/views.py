from django.shortcuts import render, redirect
from django.conf import settings
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Service, Dentist, ContactFormRequest
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def home(request):
    # Retrieve all services and dentists from the database
    services = Service.objects.all()
    dentists = Dentist.objects.all()
    # Pass the data to the template
    return render(
        request, 'home.html', {'services': services, 'dentists': dentists})


def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def contact_view(request):
    """
    Renders the Contact page and handles the contact form submission.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form_request = form.save(commit=False)
            contact_form_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for contacting us! We will get back to you shortly."
            )
            return redirect('contact')
    else:
        form = ContactForm()

    contacts = ContactFormRequest.objects.all()
    context = {
        'form': form,
        'contacts': contacts,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }

    return render(request, 'contact.html', context)
