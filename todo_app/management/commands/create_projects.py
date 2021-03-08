from django.core.management.base import BaseCommand
from mimesis import Text
from todo_app.models import Projects, Todo
from users.models import User
import random

class Command(BaseCommand):
    help = 'Create projects and todo'

    def handle(self, *args, **options):
        #GENERATE PROJECTS
        generate_project = Text('ru')
        for i in range(2):
            count_user_id = random.choice(User.objects.values_list('id'))[0]
            project = Projects(name = generate_project.word(),
                               text = generate_project.text(quantity=3))
            project.save()
            project.users.set([User.objects.get(id=str(count_user_id))])

        # GENERATE TO_DO
        generate_todo = Text('ru')
        for i in range(2):
            count_user_id = random.choice(User.objects.values_list('id'))[0]
            count_project_id = random.choice(Projects.objects.values_list('id'))[0]

            todo = Todo(todo = generate_todo.text(quantity=1),
                        text = generate_todo.text(quantity=2),
                        projects = Projects.objects.get(id=str(count_project_id)),
                        users = User.objects.get(id=str(count_user_id)))

            todo.save()


