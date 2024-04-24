from django.urls import path
from .views import RegisterUserView, ChangePasswordView, password_reset, send_email, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('password-reset/', password_reset, name='password_reset'),
    path("send-email/", send_email, name="send_mail"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
