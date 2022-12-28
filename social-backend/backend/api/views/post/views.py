from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.models import Post
from api.paginators import DefaultPaginator
from api.views.post.serializers import PostCreateSerializer, PostWithLikesSerializer


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)


class PostApiView(RetrieveAPIView):
    queryset = Post.objects.all().prefetch_related("likes")
    serializer_class = PostWithLikesSerializer
    permission_classes = (AllowAny,)


@method_decorator(cache_page(60), name="dispatch")
class PostListApiView(ListAPIView):
    queryset = Post.objects.all().prefetch_related("likes").order_by("id")
    serializer_class = PostWithLikesSerializer
    permission_classes = (AllowAny,)
    pagination_class = DefaultPaginator
