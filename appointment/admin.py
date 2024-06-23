from django.contrib import admin
from django.contrib.auth.models import User
from .models import AppointmentRequest


@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'dentist', 'service', 'date',
                    'time', 'message', 'read', 'created_at')
    list_filter = ('user', 'dentist', 'service', 'date')
    search_fields = ('user', 'dentist__name', 'service__name', 'message')
   


