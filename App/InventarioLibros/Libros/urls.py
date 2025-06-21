from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import LibrosApiView
from .ModelViewSet import LibrosViewSet
from .models import Libro

router = DefaultRouter()
router.register(r'libros',LibrosViewSet, basename='libros')

urlpatterns = [

    path('', include(router.urls)),

]