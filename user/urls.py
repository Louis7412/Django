from django.urls import path
from .views import user_register
from .views import user_login

urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
]
