from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet, ArticleModelViewSet, BiograthyModelViewSet, BookModelViewSet, \
    ProjectModelViewSet, ToDoModelViewSet


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('article', ArticleModelViewSet)
router.register('biograthy', BiograthyModelViewSet)
router.register('book', BookModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
