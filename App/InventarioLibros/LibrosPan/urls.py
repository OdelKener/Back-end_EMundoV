from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import LibrosPanApiView
from .ModelViewSet import LibrosPanViewSet
from .models import LibrosPan

router = DefaultRouter()
router.register(r'libros',LibrosPanViewSet, basename='libros')

urlpatterns = [

    path('', include(router.urls)),

]