"""
TODO
"""
from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import HomeView


# Create your tests here.

class HomeTests(SimpleTestCase):
    """TODO"""
    def setUp(self):
        """TODO"""
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_status_code(self):
        """TODO"""
        self.assertEqual(self.response.status_code, 200)

    def test_home_template(self):
        """TODO"""
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_contains_correct_html(self):
        """TODO"""
        self.assertContains(self.response, 'Home')

    def test_home_does_not_contain_incorrect_html(self):
        """TODO"""
        self.assertNotContains(self.response, 'this content should not exists')

    def test_home_url_resolves_homeview(self):
        """TODO"""
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomeView.as_view().__name__)
