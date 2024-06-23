from django.contrib import admin
from django import forms
from .models import Service, Dentist, ContactFormRequest
from django_summernote.admin import SummernoteModelAdmin


class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ['name', 'price']
    search_fields = ['name', 'price']
    ordering = ['price']
    list_filter = ('price',)


@admin.register(Dentist)
class DentistAdmin(SummernoteModelAdmin):
    list_display = ['first_name', 'last_name', 'specialty']
    search_fields = ['specialty', 'first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    list_filter = ('specialty',)


@admin.register(ContactFormRequest)
class ContactFormRequest(SummernoteModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'read']
    search_fields = ['name', 'subject']
    list_filter = ('name',)