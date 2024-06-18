from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Service, Dentist, ContactFormRequest
from .forms import ContactForm
from django.contrib import messages


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

@login_required
def contact_view(request):
    """
    Renders the Contact page and handles the contact form submission.
    """
    if request.method == "POST":
        form = ContactFormRequestForm(request.POST)
        if form.is_valid():
            contact_form_request = form.save(commit=False)
            contact_form_request.user = request.user
            contact_form_request.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for contacting us! We will get back to you shortly."
            )
            return redirect('contact')
    else:
        form = ContactForm()

    # Assuming you want to pass all contact form requests to the template
    contacts = ContactFormRequest.objects.all()

    return render(request, 'contact.html', {'form': form, 'contacts': contacts})



   
