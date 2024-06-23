
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import date, time, timedelta
from appointment.models import AppointmentRequest
from .models import AvailableTimeSlot
from clinic.models import Dentist, Service, ContactFormRequest
from .views import mark_time_slot_available, mark_time_slot_unavailable


class AppointmentRequestTests(TestCase):
    def setUp(self):
        """Creates initial objects for User, Service, Dentist, 
        and ContactFormRequest to be used in the tests."""
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.service = Service.objects.create(name='Dental Checkup', price=100.00)
        self.dentist = Dentist.objects.create(first_name='John', last_name='Doe', specialty='General Dentistry')
        self.contact_request = ContactFormRequest.objects.create(name='John Doe', email='john.doe@example.com', subject='Test Subject', message='Test Message')

    def create_appointment(self):
        """ Helper method to create an AppointmentRequest object."""
        return AppointmentRequest.objects.create(
            user=self.user,
            service=self.service,
            dentist=self.dentist,
            date=date.today(),
            time=time(10, 0),
            message='Test appointment request'
        )

    def test_appointment_list_view(self):
        """Checks if the appointment list view is accessible and uses the correct template."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('my_appointments:appointment_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_appointments/appointment_list.html')

    def test_appointment_edit_view(self):
        """Ensures the appointment edit view works and uses the correct template."""
        appointment = self.create_appointment()
        url = reverse('my_appointments:appointment_edit', args=[appointment.id])
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_appointments/appointment_edit.html')

    def test_delete_appointment_view(self):
        """ Verifies the appointment delete view is accessible and uses the correct template."""
        appointment = self.create_appointment()
        url = reverse('my_appointments:appointment_delete', args=[appointment.id])
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_appointments/appointment_delete.html')

    def test_mark_time_slot_available(self):
        """Tests marking a time slot as available"""
        test_date = date.today() + timedelta(days=1)
        test_time = time(14, 30)
        
        mark_time_slot_available(self.dentist, test_date, test_time)
        self.assertTrue(AvailableTimeSlot.objects.filter(dentist=self.dentist, date=test_date, time=test_time).exists())

    def test_mark_time_slot_unavailable(self):
        """Tests marking a time slot as unavailable."""
        test_date = date.today() + timedelta(days=2)
        test_time = time(9, 0)

        mark_time_slot_unavailable(self.dentist, test_date, test_time)
        self.assertTrue(AvailableTimeSlot.objects.filter(dentist=self.dentist, date=test_date, time=test_time).exists())











