from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from .models import Project, ToDo, User  # Author, Biograthy, Book, Article,
from .serializers import ProjectModelSerializer, ToDoModelSerializer, UserModelSerializer \
 # AuthorModelSerializer, BookModelSerializer, BiograthyModelSerializer, ArticleModelSerializer,


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


"""
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

class MyAPIView(CreateAPIView, ListAPIView):
    render_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


###
class AllProjects(CreateAPIView, ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class AllTasks(CreateAPIView, ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


"""


