"""TODO"""
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
        url = reverse('account_signup')
        self.response = self.client.get(url)
        self.username = 'newuser'
        self.email = 'newuser@email.com'

    def test_signup_template(self):
        """TODO"""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'this content should not exists')

    def test_signup_form(self):
        """TODO"""
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
