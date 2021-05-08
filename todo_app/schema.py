import graphene
from graphene_django import DjangoObjectType
from todo_app.models import Projects, Todo
from users.models import User
from uuid import uuid4


class ProjectsType(DjangoObjectType):
    class Meta:
        model = Projects
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectsType)
    all_todo = graphene.List(TodoType)
    all_users = graphene.List(UserType)
    users_by_id = graphene.Field(UserType, id=graphene.String(required=True))
    projects_by_username = graphene.List(ProjectsType, username=graphene.String(required=True))

    def resolve_all_projects(root, info):
        return Projects.objects.all()

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_users_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def resolve_projects_by_username(self, info, username):
        return Projects.objects.filter(users__username=username)


class TodoAdd(graphene.Mutation):
    class Arguments:
        todo = graphene.String(required=True)
        text = graphene.String(required=True)
        projects_id = graphene.String(required=True)
        users_id = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    @classmethod
    def mutate(cls, root, info, todo, text, projects_id, users_id):
        new_todo = Todo.objects.create(todo=todo, text=text, projects_id=projects_id,
                                       users_id=users_id)
        return TodoAdd(todo=new_todo)


class Mutation(graphene.ObjectType):
    create_todo = TodoAdd.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
