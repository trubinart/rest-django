from rest_framework.viewsets import ModelViewSet
from todo_app.models import Projects, Todo
from todo_app.serializers import ProjectsSerialaizer, TodoSerialaizer
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, TodoFilter
from rest_framework.response import Response

class ProjectLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 10

class UserLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 20

class ProjectsModelViewSet(ModelViewSet):
   queryset = Projects.objects.all()
   serializer_class = ProjectsSerialaizer
   pagination_class = ProjectLimitOffsetPagination
   filterset_class = ProjectFilter

class TodoModelViewSet(ModelViewSet):
   queryset = Todo.objects.all()
   serializer_class = TodoSerialaizer
   pagination_class = UserLimitOffsetPagination
   filterset_class = TodoFilter

   def destroy(self, request, *args, **kwargs):
      todo = Todo.objects.get(id=kwargs.get('pk'))
      todo.is_active = 'False'
      todo.save()
      serializer = TodoSerialaizer(todo)
      return Response(serializer.data)
