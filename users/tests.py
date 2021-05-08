import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from users.views import UserMixinViews

class TestUsersViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = UserMixinViews.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'Пушкин',
                                               'first_name': 'Иван',
                                               'last_name': 'Васильевич',
                                               'email': 'iva@gmail.com',
                                               'age': '87',
                                               'password': '12345',
                                               }, format='json')
        view = UserMixinViews.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
