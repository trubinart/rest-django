from rest_framework.viewsets import ModelViewSet
from todo_app.models import Projects, Todo
from todo_app.serializers import ProjectsSerialaizer, TodoSerialaizer

class ProjectsModelViewSet(ModelViewSet):
   queryset = Projects.objects.all()
   serializer_class = ProjectsSerialaizer

class TodoModelViewSet(ModelViewSet):
   queryset = Todo.objects.all()
   serializer_class = TodoSerialaizer
