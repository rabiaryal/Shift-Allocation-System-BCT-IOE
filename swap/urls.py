from django.urls import path
from .views import swap_shifts_api

urlpatterns = [
    path('swap_shifts/', swap_shifts_api, name='swap_shifts'),
]
