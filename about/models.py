from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores a single about us text
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title

