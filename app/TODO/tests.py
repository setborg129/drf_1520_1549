
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from rest_framework import status
from mixer.backend.django import mixer
from .views import ProjectViewSet
from users.models import User
from TODO.models import Project, ToDolist

# тест Джанго.
# Тестирует вью, сериализаторы и модели.
class ProjectTestCase(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_superuser(username='test', password='665sdfe4', email='test@mail.ru')
        self.project = Project.objects.create(name='Project Test')



    def test_anonim_get_project_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_get_project_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)



class TodoClientTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='test', password='665sdfe4', email='test@mail.ru')
        self.project = mixer.blend(Project)
        # self.todo = Todo.objects.create(project=self.project, todo_text='Test ToDo text', creator=self.user)
        self.todo = mixer.blend(ToDolist, todo_text='Special concrete text', project__repo_link='test mixer custom link')

    def test_anonim_get_todo_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_get_todo_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_login_logout_get_todo_list(self):
        self.client.login(username='test', password='665sdfe4')
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.client.logout()
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_todo(self):
        self.client.force_authenticate(self.user)
        response = self.client.post('/api/todo/', {"todo_text": "ToDo test POST text", "project": 1, "creator": 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_todo_id = response.data.get('id')
        new_todo = ToDolist.objects.get(pk=new_todo_id)
        self.assertEqual(new_todo.todo_text, 'ToDo test POST text')
