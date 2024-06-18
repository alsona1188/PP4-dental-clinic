from django import forms
from .models import ContactFormRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormRequest
        fields = ['name', 'email', 'subject', 'message']