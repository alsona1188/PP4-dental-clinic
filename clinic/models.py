from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    # Service model for storing services data.
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default='')

    def __str__(self):
        return self.name



