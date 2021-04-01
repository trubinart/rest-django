from django.db import models
from uuid import uuid4

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    age = models.PositiveIntegerField(null=True)
    password = models.CharField(max_length=50)



