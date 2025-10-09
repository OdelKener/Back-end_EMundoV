from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import SalidaApiView
from .ModelViewSet import SalidaViewSet, DetalleSalidaViewSet
from .models import Salida

router = DefaultRouter()
router.register(r'salida',SalidaViewSet, basename='salida')
router.register(r'detallesalida', DetalleSalidaViewSet, basename='detallesalida')

urlpatterns = [

    path('', include(router.urls)),

]