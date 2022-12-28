from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny

from api.models import Like
from api.paginators import ExtendedPaginator
from api.views.like.serializers import LikeSerializer


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
