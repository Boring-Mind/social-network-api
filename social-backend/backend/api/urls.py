from django.urls import path

from api.views import (
    UserSignupApiView,
    PostCreateApiView,
    PostWithLikesApiView,
    PostListApiView,
    LikesListApiView,
    LikeApiView,
    LikeCreateApiView,
)

app_name = "api"

urlpatterns = [
    path("signup/", UserSignupApiView.as_view(), name="user-signup"),
    path("post/", PostCreateApiView.as_view(), name="post-create"),
    path("posts/", PostListApiView.as_view(), name="posts-list"),
    path("posts/<int:pk>/", PostWithLikesApiView.as_view(), name="post-individual"),
    path("like/", LikeCreateApiView.as_view(), name="like-create"),
    path("likes/", LikesListApiView.as_view(), name="likes-list"),
    path("likes/<int:pk>/", LikeApiView.as_view(), name="like-individual"),
]
