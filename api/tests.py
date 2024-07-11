from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

    def test_signup_post_success(self):
        response = self.client.post(
            self.signup_url,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.json())
        self.assertTrue(User.objects.filter(username='testuser').exists())
        self.assertTrue(Token.objects.filter(user__username='testuser').exists())

    def test_signup_post_username_taken(self):
        User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(
            self.signup_url,
            data=json.dumps(self.user_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'username taken. choose another username'})

    def test_signup_get_not_allowed(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {'error': 'GET method is not allowed for signup.'})
