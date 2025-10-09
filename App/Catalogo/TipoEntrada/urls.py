from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import TipoEntradaApiView
from .ModelViewSet import TipoEntradaViewSet
from .models import TipoEntrada

router = DefaultRouter()
router.register(r'tipoentrada',TipoEntradaViewSet, basename='Tipoentrada')

urlpatterns = [

    path('', include(router.urls)),

]