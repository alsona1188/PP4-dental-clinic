from django.db import models
from django.contrib.auth.models import User


class AppointmentRequest(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="patient")
    service = models.ForeignKey('clinic.Service', on_delete=models.CASCADE)
    dentist = models.ForeignKey('clinic.Dentist', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Appointment request by {self.user} for {self.service.name}"
                f"with {self.dentist} on {self.date} at {self.time}")