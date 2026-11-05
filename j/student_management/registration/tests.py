from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentRegistrationTests(TestCase):
    def test_registration_page_renders(self):
        response = self.client.get(reverse('student_registration'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/Registration.html')

    def test_registration_aliases_redirect_to_canonical_url(self):
        canonical_url = reverse('student_registration')

        for alias in ('/Registration', '/Registration/'):
            with self.subTest(alias=alias):
                response = self.client.get(alias)
                self.assertRedirects(response, canonical_url)

    def test_submitting_registration_saves_student_and_shows_success(self):
        response = self.client.post(
            reverse('student_registration'),
            {
                'student_id': 'S100',
                'first_name': 'Alex',
                'last_name': 'Student',
                'gender': 'Other',
                'date_of_birth': '2005-04-12',
                'contact_number': '555-0100',
            },
        )

        self.assertRedirects(response, reverse('registration_success'))
        self.assertTrue(
            Student.objects.filter(
                student_id='S100',
                gender_name='Other',
            ).exists()
        )
