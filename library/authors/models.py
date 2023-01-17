from uuid import uuid4

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class Project(models.Model):
    name = models.CharField(max_length=32)
    link = models.TextField()
    users = models.ManyToManyField(User)
    description = models.TextField()


class ToDo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


