from django.urls import path
from .views import AuthView, LoginView, RegistrationView


urlpatterns = [
    path(
        "",
        LoginView.as_view(template_name="auth_login_basic.html"),
        name="auth-login-basic",
    ),
    path(
        "auth/register/",
        RegistrationView.as_view(template_name="auth_register_basic.html"),
        name="auth-register-basic",
    ),
    path(
        "auth/forgot_password/",
        AuthView.as_view(template_name="auth_forgot_password_basic.html"),
        name="auth-forgot-password-basic",
    ),
]
