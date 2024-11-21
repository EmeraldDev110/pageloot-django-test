from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User
from django.urls import reverse

class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a user
        self.user = User.objects.create(username="testuser", email="testuser@example.com")

        self.user_url = reverse("user-list-create")  # Define this route in your URLs

    def test_create_user(self):
        payload = {
            "username": "newuser",
            "email": "newuser@example.com"
        }
        response = self.client.post(self.user_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().username, "newuser")
        
    def test_duplicate_username(self):
        payload = {
            "username": "testuser",  # Same as the existing user
            "email": "different@example.com"
        }
        response = self.client.post(self.user_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)
        
    def test_duplicate_email(self):
        payload = {
            "username": "differentuser",
            "email": "testuser@example.com"  # Same as the existing user
        }
        response = self.client.post(self.user_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)

    

