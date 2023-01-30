import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase, APISimpleTestCase
from django.contrib.auth.models import User
from .views import UserModelViewSet, ProjectModelViewSet


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status.code, status.HTTP_200_OK)

    def test_create_quest(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users', {'first_name': 'Vasiliy', 'last_name': 'terkin', 'birthday_year': 1990})
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status.code, status.HTTP_201_CREATED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users', {'first_name': 'Vasiliy', 'last_name': 'terkin', 'birthday_year': 1990})
        admin = User.objects.create_superuser('admin', 'admin@mail.ru', 'admin')
        force_authenticate(request, admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status.code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create_user(first_name='Vasiliy', last_name='terkin', birthday_year=1990)
        client = APIClient()
        response=client.get(f'api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_edit_admin(self):
        user = User.objects.create_user(first_name='Vasiliy', last_name='terkin', birthday_year=1990)
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@mail.ru', 'admin')
        client.login(username='admin', password='admin')
        response=client.get(f'api/users/{user.id}/')
        user = User.objects.get(pk=user.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.first_name, 'Piter')
        self.assertEqual(user.last_name, 'Romanov')
        self.assertEqual(user.birthday_year, 1671)
        client.logout()

class TestProjectViewSet(APITestCase):
    def get_lists(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response, status.HTTP_200_OK)