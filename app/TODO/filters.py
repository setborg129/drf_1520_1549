from django_filters import rest_framework as filters
from .models import Project, ToDolist


class ProjectFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoFilters(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr='contains')
    project = filters.ModelChoiceFilter(field_name='project__name',
                                        to_field_name='name',
                                        queryset=Project.objects.all())
    created = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDolist
        fields = ['project']
