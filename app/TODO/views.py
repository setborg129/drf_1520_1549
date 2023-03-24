from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Project, ToDolist
from .serializers import ProjectSerializers, TodoModelSerializers

#level 4
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilters
from rest_framework.viewsets import ModelViewSet


class ToDoViewSet(ModelViewSet):
    queryset = ToDolist.objects.all()
    serializer_class = TodoModelSerializers


# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializers


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilters


# class ProjectCustomDjangoFilterViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializers
#     filter_backends = ProjectFilters
