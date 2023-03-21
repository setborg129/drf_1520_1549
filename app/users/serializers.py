# from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from .models import User, Biography, Book

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude = ()

class BiographyModelSerializers(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'
        # exclude = ()


class BookModelSerializers(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
