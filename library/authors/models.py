#from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f' {self.first_name} {self.last_name}'


class Project(models.Model):
    name = models.CharField(max_length=32)
    link = models.TextField()
    users = models.ManyToManyField(User)
    description = models.TextField()

    def __str__(self) -> str:
        return f' {self.name}'


def mark_deleted():
    return get_user_model().objects.get_or_create(active='False')[0]


class ToDo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=mark_deleted)
    active = models.BooleanField()




"""
class Author(models.Model):
    objects = None
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    birthday_year = models.PositiveIntegerField()


class Biograthy(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    author = models.ManyToManyField(Author)


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

"""


