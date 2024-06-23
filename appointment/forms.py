from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time, datetime
from .models import AppointmentRequest
from clinic.models import Dentist, Service


class TimeSelectField(forms.TypedChoiceField):
    def __init__(self, *args, **kwargs):
        self.date = kwargs.pop('date', None)
        self.dentist = kwargs.pop('dentist', None)
        super().__init__(*args, **kwargs)
        self.choices = self.get_time_choices()

    def get_time_choices(self):
        working_hours = [
            (time(9, 0), '9:00 AM'), (time(10, 0), '10:00 AM'),
            (time(11, 0), '11:00 AM'), (time(12, 0), '12:00 PM'),
            (time(14, 0), '2:00 PM'), (time(15, 0), '3:00 PM'),
            (time(16, 0), '4:00 PM'), (time(17, 0), '5:00 PM')
        ]

        if self.date and self.dentist:
            booked_times = AppointmentRequest.objects.filter(
                dentist=self.dentist, date=self.date).values_list(
                    'time', flat=True)
            working_hours = [slot for slot in working_hours
                             if slot[0] not in booked_times]

        return working_hours

    def valid_value(self, value):
        text_value = str(value)
        for k, v in self.choices:
            if value == k or text_value == str(k):
                return True
        return False


class AppointmentForm(forms.ModelForm):
    time = TimeSelectField(label='Time')

    class Meta:
        model = AppointmentRequest
        fields = ('service', 'dentist', 'date', 'time', 'message')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'date' in self.data and 'dentist' in self.data:
            date = self.data.get('date')
            dentist = self.data.get('dentist')
            self.fields['time'] = TimeSelectField(date=date, dentist=dentist)

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date.weekday() in (5, 6):  # 5 = Saturday, 6 = Sunday
            raise ValidationError(
                "Appointments cannot be booked on weekends.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        dentist = cleaned_data.get('dentist')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if dentist and date and time:
            if AppointmentRequest.objects.filter(
                 dentist=dentist, date=date, time=time).exists():
                raise ValidationError(
                    "This time slot is already booked")

        return cleaned_data
