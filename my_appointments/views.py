from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from appointment.forms import AppointmentForm
from appointment.models import AppointmentRequest
from .models import AvailableTimeSlot

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
            old_time = appointment.time
            new_appointment = appointment_form.save(commit=False)
            new_time = new_appointment.time
            new_appointment.save()
            messages.add_message(request, messages.SUCCESS, 'Appointment updated successfully.')
            return redirect('my_appointments:appointment_list')
            if old_time != new_time:
                # Mark the old time slot as available
                mark_time_slot_available(appointment.dentist, appointment.date, old_time)
                return HttpResponseRedirect(reverse('my_appointments:appointment_list', args=(appointment_id,)))
    else:
        appointment_form = AppointmentForm(instance=appointment) 
    return render(request, 'my_appointments/appointment_edit.html', {'appointment_form': appointment_form})



def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentRequest, pk=appointment_id)
    if request.method == 'POST':
        # Mark the time slot as available before deleting
        mark_time_slot_available(appointment.dentist, appointment.date, appointment.time)
        appointment.delete()
        messages.add_message(request, messages.SUCCESS, 'Your appointment was deleted successfully.')
        return HttpResponseRedirect(reverse('my_appointments:appointment_list'))
    return render(request, 'my_appointments/appointment_delete.html', {'appointment': appointment})


def mark_time_slot_available(dentist, date, time):
    # Add a new AvailableTimeSlot entry for the given dentist, date, and time
    AvailableTimeSlot.objects.create(dentist=dentist, date=date, time=time)

   
