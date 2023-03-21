from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import User, Biography, Book
from .serializers import UserSerializers, BiographyModelSerializers, BookModelSerializers


class UserSerializers(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializers


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers
