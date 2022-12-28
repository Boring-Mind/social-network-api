from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Post, Like
from api.paginators import DefaultPaginator, ExtendedPaginator
from api.serializers import (
    UserSerializer,
    PostSerializer,
    PostWithLikesSerializer,
    LikeSerializer,
)


class UserSignupApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class PostWithLikesApiView(RetrieveAPIView):
    queryset = Post.objects.all().prefetch_related("likes")
    serializer_class = PostWithLikesSerializer
    permission_classes = (AllowAny,)


@method_decorator(cache_page(60), name="dispatch")
class PostListApiView(ListAPIView):
    queryset = Post.objects.all().prefetch_related("likes").order_by("id")
    serializer_class = PostWithLikesSerializer
    permission_classes = (AllowAny,)
    pagination_class = DefaultPaginator


class LikesListApiView(ListAPIView):
    queryset = Like.objects.all().order_by("id")
    serializer_class = LikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = ExtendedPaginator


class LikeCreateApiView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (AllowAny,)


class LikeApiView(RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (AllowAny,)
