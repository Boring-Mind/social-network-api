from django.urls import path

from api.views import UserSignupApiView, PostCreateApiView, UserActivityApiView

app_name = "api"

urlpatterns = [
    path("signup/", UserSignupApiView.as_view(), name="user-signup"),
    path("post/", PostCreateApiView.as_view(), name="post"),
    path("user_activity/", UserActivityApiView.as_view(), name="user-activity"),
]
