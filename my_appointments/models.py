from django.db import models
from clinic.models import Dentist

# Create your models here.


class AvailableTimeSlot(models.Model):
    """Represents the availability of time slots for a dentist.
    Is used to manage and track which time slots are available
    for booking appointments with a specific dentist on a given date and time"""
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.dentist} available on {self.date} at {self.time}"
