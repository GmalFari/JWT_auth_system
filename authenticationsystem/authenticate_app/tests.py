from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserAccount
from django.contrib.auth.models import Group
from rest_framework_simplejwt.tokens import RefreshToken

class UserAccountAPITest(TestCase):
  
    def setUp(self):
          self.client = APIClient()

          # Create a Group object
          group, _ = Group.objects.get_or_create(name='usersGroup')

          self.user1 = UserAccount.objects.create(
              first_name='Jamal',
              last_name='Farea', 
              email='Jamal@gmail.com',
              password="pass123."
              # group=group  # Assign the created group to the user
          )

          self.user2 = UserAccount.objects.create(
            first_name='Jamal',
            last_name='Farea',
            email='jamal@yahoo.com',
            password="pass123."

            # group=group  # Assign the created group to the user
        )

    def test_create_user_account(self):
        url = 'http://localhost:8000/api/auth/accounts/'
        data = {
            'first_name': 'First',
            'last_name': 'name',
            'email': 'first@gmail.com',
            'user_type': 'normal',
            'password': 'pass123.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserAccount.objects.count(), 3)

    def test_get_user_account(self):
        url = f'http://localhost:8000/api/auth/accounts/{self.user1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jamal')
        self.assertEqual(response.data['last_name'], 'Farea')
        self.assertEqual(response.data['email'], 'Jamal@gmail.com')
        self.assertEqual(response.data['user_type'], 'normal')

    def test_update_user_account(self):
        url = f'http://localhost:8000/api/auth/accounts/{self.user2.id}/'
        data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'updated@gmail.com',
            'user_type': 'admin'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Updated')
        self.assertEqual(response.data['last_name'], 'Name')
        self.assertEqual(response.data['email'], 'updated@gmail.com')
        self.assertEqual(response.data['user_type'], 'admin')

    def test_invalid_email_validation(self):
        url = 'http://localhost:8000/api/auth/accounts/'
        data = {
            'first_name': 'Invalid',
            'last_name': 'Email',
            'email': 'invalidemail',
            'user_type': 'customer',
            'password': 'pass123.'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], 'Enter a valid email address.')
