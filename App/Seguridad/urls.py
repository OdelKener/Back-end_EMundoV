from django.urls import path, include

urlpatterns = [

    path('Usuarios/', include('App.Seguridad.Usuario.urls')),
    
]