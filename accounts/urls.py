from django.urls import path
from accounts.views import SignUpView
from django.contrib.auth import views as auth_views
# app_name = accounts

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='change-password.html'),
    ),
]