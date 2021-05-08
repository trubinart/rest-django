from django.db import models
from uuid import uuid4
from users.models import User

# Create your models here.

class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=56, unique=True)
    text = models.TextField(max_length=128, blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Проект: {self.name}, с пользователями: ({self.users})"


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    todo = models.CharField(max_length=128)
    text = models.TextField(max_length=256, blank=True)
    projects = models.ForeignKey(Projects, on_delete = models.CASCADE)
    users = models.ForeignKey(User, on_delete = models.CASCADE)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TODO: {self.todo} от {self.create_date})"

