from django import forms
from .models import AppointmentRequest
from datetime import time

class TimeSelectField(forms.TypedChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self.get_time_choices()

    def get_time_choices(self):
        working_hours = [(time(9, 0), '9:00 AM'), (time(10, 0), '10:00 AM'), (time(11, 0), '11:00 AM'), (time(12, 0), '12:00 PM'),
                         (time(14, 0), '2:00 PM'), (time(15, 0), '3:00 PM'), (time(16, 0), '4:00 PM'), (time(17, 0), '5:00 PM')]
        return working_hours

class AppointmentForm(forms.ModelForm):
    time = TimeSelectField(label='Time')

    class Meta:
        model = AppointmentRequest
        fields = ('full_name', 'service', 'dentist', 'date', 'time', 'message')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }