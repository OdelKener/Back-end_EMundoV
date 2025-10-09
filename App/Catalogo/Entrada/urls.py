from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import EntradaApiView
from .ModelViewSet import EntradaViewSet, DetalleEntradaViewSet

from .models import Entrada

router = DefaultRouter()
router.register(r'entrada',EntradaViewSet, basename='entrada')
router.register(r'detalleentrada', DetalleEntradaViewSet, basename='detalleentrada')



urlpatterns = [

    path('', include(router.urls)),

]