from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .models import ContactFormRequest


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_form_submission(self):
        # Sends a POST request to the contact_view with valid data.
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'subject': 'Testing contact form',
            'message': 'This is a test message.'
        }

        # Submit POST request
        response = self.client.post(reverse('contact'), data)

        # Check if the form submission was successful
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactFormRequest.objects.count(), 1)

        # Retrieve the created ContactFormRequest object
        contact_form_request = ContactFormRequest.objects.first()

        # Verify the data saved in the object
        self.assertEqual(contact_form_request.name, 'John Doe')
        self.assertEqual(contact_form_request.email, 'johndoe@example.com')
        self.assertEqual(contact_form_request.subject, 'Testing contact form')
        self.assertEqual(
            contact_form_request.message, 'This is a test message.')

    def test_contact_form_invalid_submission(self):
        """Tests handling of invalid form submissions.
        Sends a POST request with invalid data"""
        invalid_data = {
            'name': '',  # Invalid because name is required
            'email': 'invalid-email',  # Invalid email format
            'subject': 'Testing contact form',
            'message': 'This is a test message.'
        }

        # Submit POST request with invalid data
        response = self.client.post(reverse('contact'), invalid_data)

        # Check if the form submission failed and no new object was created
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactFormRequest.objects.count(), 0)

        # Optionally, check for error messages or form errors in the response
        self.assertFormError(
            response, 'form', 'email', 'Enter a valid email address.')
