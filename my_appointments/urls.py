from . import views
from django.urls import path

app_name = 'my_appointments'

urlpatterns = [
    
    path('my_appointments/', views.appointment_list, name='appointment_list'),
    
]