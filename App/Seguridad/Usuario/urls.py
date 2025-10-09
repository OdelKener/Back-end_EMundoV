from django.urls import path
from App.Seguridad.Usuario.views import UserCreateView,LoginUView

urlpatterns = [
    path('RegistroU/', UserCreateView.as_view(), name='register-user'),
    path('LoginU/', LoginUView.as_view(), name='login-user' )
]