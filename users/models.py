from django.db import models
from uuid import uuid4
from mimesis import Person

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=50)


# person = Person('en')
# for i in range (0,10):
#     user = User(first_name=person.first_name(), last_name=person.last_name(),
#                 email=person.email(), age=person.age(), password=person.password())
#     user.save()