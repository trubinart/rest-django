from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todo_app.views import ProjectsModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectsModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
]
