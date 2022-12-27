from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Post
from api.paginators import DefaultPaginator
from api.serializers import (
    UserSerializer,
    PostSerializer,
    UserActivitySerializer,
    PostWithLikesSerializer,
)


class UserSignupApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


@method_decorator(cache_page(30), name="dispatch")
class UserActivityApiView(ListAPIView):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserActivitySerializer
    permission_classes = (AllowAny,)
    pagination_class = DefaultPaginator


@method_decorator(cache_page(30), name="dispatch")
class PostWithLikesApiView(RetrieveAPIView):
    queryset = Post.objects.all().prefetch_related("likes")
    serializer_class = PostWithLikesSerializer
    permission_classes = (AllowAny,)


@method_decorator(cache_page(30), name="dispatch")
class PostListApiView(ListAPIView):
    queryset = Post.objects.all().prefetch_related("likes").order_by("id")
    serializer_class = PostWithLikesSerializer
    permission_classes = (AllowAny,)
    pagination_class = DefaultPaginator
