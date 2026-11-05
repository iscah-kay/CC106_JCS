from django.test import TestCase


class LandingPageTests(TestCase):
    def test_landing_page_renders(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/landing.html')

    def test_home_page_renders_and_links_to_landing(self):
        response = self.client.get('/home/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
        self.assertContains(response, 'href="/"')

    def test_home_without_trailing_slash_redirects_to_canonical_url(self):
        response = self.client.get('/home')

        self.assertRedirects(response, '/home/', status_code=301)

    def test_legacy_home_url_redirects_to_canonical_url(self):
        response = self.client.get('/Home/')

        self.assertRedirects(response, '/home/')

    def test_landing_page_links_to_home(self):
        response = self.client.get('/')

        self.assertContains(response, 'href="/home/"')
