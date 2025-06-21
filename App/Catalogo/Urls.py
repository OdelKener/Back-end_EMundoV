from django.urls import path, include





urlpatterns=[

path('Entrada/', include('App.Catalogo.Entrada.urls')),


path('Salida/', include('App.Catalogo.Salida.urls')),
path('TipoEntrada/', include('App.Catalogo.TipoEntrada.urls')),
path('TipoSalida/', include('App.Catalogo.TipoSalida.urls')),
]

