from django.test import TestCase
from .models import CustomUser
# Create your tests here.


class CustomUserModelTest(TestCase):

    def test_custom_user_creation(self):
        user = CustomUser.objects.create(email='test@example.com', role='customer')
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.role, 'customer')

    def test_custom_user_full_name(self):
        user = CustomUser.objects.create(email='test@example.com', first_name='John', last_name='Doe', role='customer')
        self.assertEqual(user.get_full_name(), 'John Doe')

    def test_custom_user_str_representation(self):
        user = CustomUser.objects.create(email='test@example.com', role='customer')
        self.assertEqual(str(user), 'test@example.com')