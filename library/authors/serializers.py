from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, ToDo, User  # Author, Biograthy, Book, Article,


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ('first_name', 'birthday_year')
        # exclude = ['first_name']


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # ('first_name', 'birthday_year')


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'  # ('first_name', 'birthday_year')
