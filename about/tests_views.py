from django.test import TestCase
from django.urls import reverse
from .models import About
from django.utils import timezone
from datetime import timedelta


class AboutUsViewTest(TestCase):

    def setUp(self):
        # Create a sample About object for testing
        self.about = About.objects.create(
            title="Test About Us",
            updated_on=timezone.now() - timedelta(days=1),  # Simulate a date in the past
            content="This is a test about us content.",
        )

    def test_about_us_view(self):
        url = reverse('about')  # Assuming 'about_us' is the name of your URL pattern
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)  # Check if the page loads successfully
        self.assertContains(response, self.about.title)  # Check if the title appears in the rendered HTML
        self.assertContains(response, self.about.content)  # Check if the content appears in the rendered HTML

    def tearDown(self):
        # Clean up any resources after each test if needed
        pass

