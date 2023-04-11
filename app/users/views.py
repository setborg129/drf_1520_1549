from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import User, Biography, Book
from .serializers import UserSerializers, BiographyModelSerializers, BookModelSerializers, UserAuthSerializer
from django.contrib.auth.models import User as AuthUser

#level 4
from rest_framework.viewsets import mixins, GenericViewSet


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializers


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializers





class UserViewSet(mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  # mixins.CreateModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserAuthSerializer
        return UserSerializers

    def get_queryset(self):
        if self.request.version == '0.2':
            return AuthUser.objects.all()
        return User.objects.all()
