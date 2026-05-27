from django.test import TestCase
from django.contrib.auth.models import User

class AuthTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):
        login = self.client.login(username='testuser', password='testpass')
        self.assertTrue(login)
        
    def test_logout(self):
        self.client.login(username='testuser', password='testpass')
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
