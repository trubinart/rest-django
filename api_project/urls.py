from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserMixinViews
from todo_app.views import ProjectsModelViewSet, TodoModelViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('users', UserMixinViews)
router.register('projects', ProjectsModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
   path('api-token-auth/', views.obtain_auth_token),

]
