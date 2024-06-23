from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import AppointmentForm
from .models import AppointmentRequest


class AppointmentRequestViewTests(TestCase):

    def setUp(self):
        """This method is where you set up any prerequisites for your tests.
         Here, we create a test user using Django's authentication system."""
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_appointment_request_view_get(self):
        """Tests the GET request to your view. 
        It checks that the view returns a status code of 200 (OK) 
        and uses the correct template."""
        self.client.force_login(self.user)  # Simulate logged in user
        response = self.client.get(reverse('appointment')) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment/appointment.html')

    
