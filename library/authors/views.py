from rest_framework.viewsets import ModelViewSet
from .models import Author, Biograthy, Book, Article, Project, ToDo
from .serializers import AuthorModelSerializer, BookModelSerializer, BiograthyModelSerializer, ArticleModelSerializer, \
    ProjectModelSerializer, ToDoModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiograthyModelViewSet(ModelViewSet):
    queryset = Biograthy.objects.all()
    serializer_class = BiograthyModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
