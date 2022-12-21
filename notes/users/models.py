from uuid import uuid4

from django.db import models


class User(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    e_mail = models.CharField(max_length=30, unique=True)
