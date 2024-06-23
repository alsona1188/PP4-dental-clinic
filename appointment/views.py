from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import AppointmentForm
from .models import AppointmentRequest
from django.contrib import messages


@login_required
def appointment_request(request):
    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            appointment_form = AppointmentForm()
            messages.success(request, "Thank you for booking with us!")
        else:
            messages.error(request,
                           "This time slot is not available! "
                           "Try another one, or you can call us: "
                           "+49 345 678912")
    else:
        appointment_form = AppointmentForm()

    return render(
        request,
        "appointment/appointment.html",
        {
            "appointment_form": appointment_form
        },
    )
