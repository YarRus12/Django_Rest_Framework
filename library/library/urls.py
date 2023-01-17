from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from authors.views import ProjectModelViewSet, ToDoModelViewSet, UserModelViewSet
# AuthorModelViewSet, ArticleModelViewSet, BiograthyModelViewSet, BookModelViewSet, MyAPIView, AllProjects, AllTasks

router = DefaultRouter()

router.register('users', UserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

# router.register('authors', AuthorModelViewSet)
# router.register('article', ArticleModelViewSet)
# router.register('biograthy', BiograthyModelViewSet)
# router.register('book', BookModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('project/', ProjectModelViewSet.as_view(({'get': 'list'}))),
]
