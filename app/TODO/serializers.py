from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, ToDolist

class ProjectSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = ToDolist
        fields = '__all__'




