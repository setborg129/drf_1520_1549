from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Project, ToDolist
from .serializers import ProjectSerializers, TodoModelSerializers


class ToDoViewSet(ModelViewSet):
    queryset = ToDolist.objects.all()
    serializer_class = TodoModelSerializers


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
