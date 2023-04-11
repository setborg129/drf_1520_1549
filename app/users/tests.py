import math

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
from django.contrib.auth.models import User

from users.views import UserViewSet
from users.models import User, Biography, Book


class TestUsersViewSet(TestCase):
    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'asdasd'
        self.email = 'admin@mail.ru'
        self.data = {'first_name': 'Александр', 'last_name': 'Пушкин', 'Birthday_year': 1799}
        self.data_p = {'first_name': 'Николай', 'last_name': 'Нагорный', 'Birthday_year': 1799}
        self.url = '/api/users/'
        self.admin = User.Objects.create_superuser(username=self.name, password=self.password, email=self.email)

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
