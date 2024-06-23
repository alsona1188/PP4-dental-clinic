from django.urls import path
from . import views

app_name = 'my_appointments'

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('appointment/<int:pk>/edit/',
         views.appointment_edit, name='appointment_edit'),
    path('appointments/delete/<int:appointment_id>/',
         views.delete_appointment, name='appointment_delete'),
]

