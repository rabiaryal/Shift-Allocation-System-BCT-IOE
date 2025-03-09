from django.urls import path
from .views_old import HRManagerAPI
from .views import *

urlpatterns = [
    # path('login/', HRManagerAPI.as_view(), name='login_api'),
    path('api/auth/register', RegisterView.as_view(), name = 'register_api'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('api/auth/login', LoginView.as_view(), name = 'login_api'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
