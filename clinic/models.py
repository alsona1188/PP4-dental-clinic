from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Service(models.Model):
    # Service model for storing services data.
    name = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class Dentist(models.Model):
    # Dentist model for storing the dentist's data.
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200)
    services = models.ManyToManyField('Service', related_name='dentists')
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'


class ContactFormRequest(models.Model):
    # Contact form model for storing the contact forms data.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contact_forms")
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact form request by {self.user.username} with subject {self.subject}"



