from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from appointment.forms import AppointmentForm
from appointment.models import AppointmentRequest

# Create your views here.

def appointment_list(request):
    appointments = AppointmentRequest.objects.filter(user=request.user)
    return render(request, 'my_appointments/appointment_list.html', {'appointments': appointments})


@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(AppointmentRequest, pk=pk, user=request.user)
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST, instance=appointment)
        if appointment_form.is_valid():
            appointment_form.save()
            messages.add_message(request, messages.SUCCESS, 'Appointment updated successfully.')
            return redirect('my_appointments:appointment_list')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to update the appointment. Please check the form.')
    else:
        appointment_form = AppointmentForm(instance=appointment) 
    return render(request, 'my_appointments/appointment_edit.html', {"appointment_form": appointment_form})
