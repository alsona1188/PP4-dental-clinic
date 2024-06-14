
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from appointment.forms import AppointmentForm
from appointment.models import AppointmentRequest

# Create your views here.

def appointment_list(request):
    appointments = AppointmentRequest.objects.filter(user=request.user)
    return render(request, 'my_appointments/appointment_list.html', {'appointments': appointments})