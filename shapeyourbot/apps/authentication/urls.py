from django.urls import path
from .views import RegistrationView, ChangePasswordView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("login/", obtain_auth_token, name="login"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password")
]