from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from authors.views import ToDoModelViewSet, UserModelViewSet, ProjectFilterViewSet
from rest_framework.authtoken.views import obtain_auth_token
import re

router = DefaultRouter()

router.register('users', UserModelViewSet, basename='users')
router.register('todo', ToDoModelViewSet)
router.register('projects', ProjectFilterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),

]
