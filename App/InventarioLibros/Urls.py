from django.urls import path, include





urlpatterns=[


path('Libros/', include('App.InventarioLibros.Libros.urls')),
path('LibrosCos/', include('App.InventarioLibros.LibrosCos.urls')),
path('LibrosHon/', include('App.InventarioLibros.LibrosHon.urls')),
path('LibrosPan/', include('App.InventarioLibros.LibrosPan.urls')),
path('Categorias/', include('App.InventarioLibros.Categorias.Urls')),

]

