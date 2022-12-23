from django.urls import path

from api.views import UserSignupApiView

app_name = "api"

urlpatterns = [
    path("signup/", UserSignupApiView.as_view(), name="user-signup"),
]
