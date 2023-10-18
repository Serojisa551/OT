from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)




urlpatterns = [
    path("", main_page, name="main_page"),
    path("register/", register_users, name="register_users"),
    path("authentic/", authentic_user, name="authentic_user"),
    path("logout/", logout_request, name="logout_request"),
    path("password_reset/", send_mail, name="password_reset_email"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]