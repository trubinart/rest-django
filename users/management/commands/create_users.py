from django.core.management.base import BaseCommand
from mimesis import Person
from users.models import User

class Command(BaseCommand):
    help = 'Create users'

    def handle(self, *args, **options):
        person = Person('ru')
        for i in range(2):
            user = User(username=person.username(),
                        first_name= person.first_name(),
                        last_name = person.last_name(),
                        email = person.email(),
                        age = person.age(),
                        password = person.password())
            user.save()