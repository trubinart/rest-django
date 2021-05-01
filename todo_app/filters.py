from django_filters import rest_framework as filters
from .models import Projects, Todo

class ProjectFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Projects
       fields = ('name',)


class TodoFilter(filters.FilterSet):
   todo = filters.CharFilter(lookup_expr='contains')
   create_date = filters.DateFromToRangeFilter()
   class Meta:
       model = Todo
       fields = ('todo', 'create_date')