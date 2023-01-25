from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, get_object_or_404
from rest_framework.response import Response
from .models import Project, ToDo, User  # Author, Biograthy, Book, Article,
from .serializers import ProjectModelSerializer, ToDoModelSerializer, UserModelSerializer \
    # AuthorModelSerializer, BookModelSerializer, BiograthyModelSerializer, ArticleModelSerializer,

# Собственные классы пагинации


class ProjectPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoPagination(LimitOffsetPagination):
    default_limit = 20


class UserModelViewSet(viewsets.ViewSet):
    # renderer_classes = [JSONRenderer]

    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass


class ProjectFilterViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()

    def get_queryset(self):
        return Project.objects.filter(name__contains='name')


class ProjectModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = ToDoPagination
    filter_fields = ['project']
