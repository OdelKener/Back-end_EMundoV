from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import LibrosApiView
from .ModelViewSet import LibrosCosViewSet
from .models import LibrosCos

router = DefaultRouter()
router.register(r'libros',LibrosCosViewSet, basename='libros')

urlpatterns = [

    path('', include(router.urls)),

]