from django.contrib import admin
from django.contrib.auth.models import User
from .models import AppointmentRequest


@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name','dentist', 'service', 'date', 'time', 'message', 'read', 'created_at')
    list_filter = ('full_name','dentist', 'service', 'date')
    search_fields = ('full_name','dentist__name', 'service__name', 'message')
   


