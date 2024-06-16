from django.db import models
from clinic.models import Dentist

# Create your models here.

class AvailableTimeSlot(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.dentist} available on {self.date} at {self.time}"