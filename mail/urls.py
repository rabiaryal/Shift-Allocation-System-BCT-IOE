from django.urls import path, include
from .views import *

urlpatterns = [
    path('sendmail', SendEmailView.as_view(), name='send_email'),
]
