from django.db import models
from django.contrib.auth.models import User


class AppointmentRequest(models.Model):
    full_name = models.CharField(max_length=200, default="Please enter your name")
    service = models.ForeignKey('clinic.Service', on_delete=models.CASCADE)
    dentist = models.ForeignKey('clinic.Dentist', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment request by {self.full_name} for {self.service.name} with {self.dentist} on {self.date} at {self.time}"