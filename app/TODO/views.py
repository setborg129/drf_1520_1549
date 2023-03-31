from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Project, ToDolist
from .serializers import ProjectSerializers, TodoModelSerializers

# level 4
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilters, TodoFilters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


#lesson_6
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, \
    BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.username


# class ToDoViewSet(ModelViewSet):
#     queryset = ToDolist.objects.all()
#     serializer_class = TodoModelSerializers


# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializers


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilters


class ToDoViewSet(ModelViewSet):
    queryset = ToDolist.objects.all()
    serializer_class = TodoModelSerializers
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilters

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

# class ProjectCustomDjangoFilterViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializers
#     filter_backends = ProjectFilters
