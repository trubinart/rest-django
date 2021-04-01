import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectsModelViewSet, TodoModelViewSet
from .models import Projects, Todo

class TestProjectsModelViewSet(TestCase):

    def test_get_project(self):
        client = APIClient()
        response = client.get(f'/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestTodoModelViewSet(TestCase):

    def test_get_todo_autorizate(self):
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.get(f'/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()

class TestProjectsModelViewSetTestCase(APITestCase):

    def test_get_project(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        project = Projects.objects.create(name='тест',
                                          text= 'тест текста')
        self.client.login(username='admin', password='admin123456')
        response = self.client.patch(f'/api/projects/{project.id}/', {'name': 'изменен'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)