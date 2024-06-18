from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from appointment.forms import AppointmentForm
from appointment.models import AppointmentRequest
from .models import AvailableTimeSlot
from appointment.forms import TimeSelectField

# Create your views here.

@login_required
def appointment_list(request):
    appointments = AppointmentRequest.objects.filter(user=request.user)
    return render(request, 'my_appointments/appointment_list.html', {'appointments': appointments})


@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(AppointmentRequest, pk=pk, user=request.user)
    if request.method == "POST":
        appointment_form = AppointmentForm(request.POST, instance=appointment)
        if appointment_form.is_valid():
            new_appointment = appointment_form.save(commit=False)
            new_time = new_appointment.time
            new_date = new_appointment.date

            # Check if time has changed
            if appointment.time != new_time or appointment.date != new_date:
                # Mark the old time slot as available
                mark_time_slot_available(appointment.dentist, appointment.date, appointment.time)

            new_appointment.save()
            messages.add_message(request, messages.SUCCESS, 'Appointment updated successfully.')

            # Mark the new time slot as unavailable
            mark_time_slot_unavailable(new_appointment.dentist, new_date, new_time)

            return redirect('my_appointments:appointment_list')
    else:
        # Initialize the form with the appointment data and specify the date and dentist
        appointment_form = AppointmentForm(instance=appointment, initial={'date': appointment.date, 'dentist': appointment.dentist})

        # Pass the date and dentist to the TimeSelectField
        appointment_form.fields['time'] = TimeSelectField(date=appointment.date, dentist=appointment.dentist)

    return render(request, 'my_appointments/appointment_edit.html', {'appointment_form': appointment_form})



@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentRequest, pk=appointment_id, user=request.user)
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


def mark_time_slot_unavailable(dentist, date, time):
    # Check if the new time slot already exists
    if not AvailableTimeSlot.objects.filter(dentist=dentist, date=date, time=time).exists():
        # Add a new AvailableTimeSlot entry for the given dentist, date, and time
        AvailableTimeSlot.objects.create(dentist=dentist, date=date, time=time)
