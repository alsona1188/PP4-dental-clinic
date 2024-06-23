from django.shortcuts import render
from .models import About

# Create your views here. 

def about_us(request):
    """
    Renders the About page.
    It queries the database for the latest About object based on the updated_on field, 
    and then renders it using the about/about.html
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )


