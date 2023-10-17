from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("register/", register_users, name="register_users"),
    path("authentic/", authentic_user, name="authentic_user"),
    path("logout/", logout_request, name="logout_request"),
]