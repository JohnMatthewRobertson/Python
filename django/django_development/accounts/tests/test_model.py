"""TODO"""
from accounts.forms import CustomUserCreationForm
from accounts.views import SignupView
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


# Create your tests here.

class CustomUserTests(TestCase):
    """TODO"""

    def test_create_standard_user(self):
        """TODO"""
        user_standard = get_user_model()
        user = user_standard.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_admin_user(self):
        """TODO"""
        user_admin = get_user_model()
        user = user_admin.objects.create_superuser(username='superadmin',
                                                   email='superadmin@email.com',
                                                   password='testpass123'
                                                   )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupTests(TestCase):
    """TODO"""

    def setUp(self):
        """TODO"""
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        """TODO"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'this content should not exists')

    def test_signup_form(self):
        """TODO"""
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        """TODO"""
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__, SignupView.as_view().__name__
        )
