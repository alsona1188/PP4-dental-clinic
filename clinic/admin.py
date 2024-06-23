from django.contrib import admin
from django import forms
from .models import Service, Dentist, ContactFormRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']
    ordering = ['price'] 
    summernote_fields = ('description',)
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


