from rest_framework import mixins, viewsets
from users.models import User
from users.serializers import UserModelSerializer, UserModelSerializerAdvanced

class UserMixinViews(mixins.ListModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2.0':
            print(self.request.version)
            return UserModelSerializerAdvanced
        return UserModelSerializer


