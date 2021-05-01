from rest_framework.viewsets import ModelViewSet
from todo_app.models import Projects, Todo
from todo_app.serializers import ProjectsSerialaizer, TodoSerialaizer, ProjectsSerialaizerBase
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, TodoFilter
from rest_framework.response import Response
from users.models import User
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

class ProjectLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 10

class UserLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 20

class ProjectsModelViewSet(ModelViewSet):
   queryset = Projects.objects.all()
   serializer_class = ProjectsSerialaizer
   pagination_class = ProjectLimitOffsetPagination
   filterset_class = ProjectFilter

   def get_serializer_class(self):
      if self.request.method in ['GET']:
         return ProjectsSerialaizerBase
      return ProjectsSerialaizer

   def create(self, request, *args, **kwargs):
      print(request.data)
      user = User.objects.get(id=request.data['users'][0]['id'])
      new_project = Projects(name=request.data['name'], text=request.data['text'])
      new_project.save()
      new_project.users.set([user])
      serializer = ProjectsSerialaizer(new_project)
      return Response(serializer.data)

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
