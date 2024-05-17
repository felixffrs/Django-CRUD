from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class TestSetUp(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user).key
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }
        return super().setUp()

