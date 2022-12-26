from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Post
from api.serializers import UserSerializer, PostSerializer


class UserSignupApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @never_cache
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    @never_cache
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
