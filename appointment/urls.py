from . import views
from django.urls import path


urlpatterns = [
    path('', views.appointment_request, name='appointment'),
]