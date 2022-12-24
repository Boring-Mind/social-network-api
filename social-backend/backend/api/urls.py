from django.urls import path

from api.views import UserSignupApiView, PostCreateApiView

app_name = "api"

urlpatterns = [
    path("signup/", UserSignupApiView.as_view(), name="user-signup"),
    path("post/", PostCreateApiView.as_view(), name="post"),
]
