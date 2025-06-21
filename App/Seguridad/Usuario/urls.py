from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('RegistroU/', UserCreateView.as_view(), name='register-user'),
]