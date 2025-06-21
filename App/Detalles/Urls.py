from django.urls import  path, include

urlpatterns = [


    path('DetalleEntrada/', include('App.Detalles.DetalleEntrada.urls')),
    path('DetalleSalida/', include('App.Detalles.DetalleSalida.urls')),
]