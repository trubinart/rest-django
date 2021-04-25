from rest_framework.serializers import ModelSerializer
from todo_app.models import Projects, Todo
from users.models import User


class UserSerialaizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)

class ProjectsSerialaizer(ModelSerializer):
    users = UserSerialaizer(many=True)

    class Meta:
        model = Projects
        fields = '__all__'

class ProjectsSerialaizerBase(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class TodoSerialaizer(ModelSerializer):
    projects = ProjectsSerialaizer()
    users = UserSerialaizer()

    class Meta:
        model = Todo
        fields = '__all__'

