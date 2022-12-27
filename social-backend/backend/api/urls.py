from django.urls import path

from api.views import (
    UserSignupApiView,
    PostCreateApiView,
    UserActivityApiView,
    PostWithLikesApiView,
    PostListApiView,
)

app_name = "api"

urlpatterns = [
    path("signup/", UserSignupApiView.as_view(), name="user-signup"),
    path("post/", PostCreateApiView.as_view(), name="post-create"),
    path("posts/", PostListApiView.as_view(), name="posts-list"),
    path("user_activity/", UserActivityApiView.as_view(), name="user-activity"),
    path("post/<int:pk>/", PostWithLikesApiView.as_view(), name="post-individual"),
]
