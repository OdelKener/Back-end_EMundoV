from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import DetalleEntradaApiView
from .ModelViewSet import DetalleEntradaViewSet
from .models import DetalleEntrada

router = DefaultRouter()
router.register(r'detallentrada',DetalleEntradaViewSet, basename='detalleentrada')

urlpatterns = [

    path('', include(router.urls)),

]