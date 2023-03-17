from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializers

class UserSerializers(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
