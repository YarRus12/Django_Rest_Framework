from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Biograthy, Book, Article, Project, ToDo


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'  # ('first_name', 'birthday_year')
        # exclude = ['first_name']


class BiograthyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biograthy
        fields = '__all__'  # ('first_name', 'birthday_year')


class BookModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # ('first_name', 'birthday_year')


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer() # Выводим не только id но и все поля, выдаваемые сериализатором
    class Meta:
        model = Article
        fields = '__all__'  # ('first_name', 'birthday_year')


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # ('first_name', 'birthday_year')


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'  # ('first_name', 'birthday_year')
