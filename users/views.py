from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets
from users.models import User
from users.serializers import UserModelSerializer
import logging


class UserMixinViews(mixins.ListModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet, mixins.RetrieveModelMixin):
   queryset = User.objects.all()
   serializer_class = UserModelSerializer