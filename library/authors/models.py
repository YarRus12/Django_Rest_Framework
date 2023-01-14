from uuid import uuid4

from django.db import models


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


class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=32)
    author = models.ManyToManyField(Author)


class ToDo(models.Model):
    record = models.CharField(max_length=32)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
