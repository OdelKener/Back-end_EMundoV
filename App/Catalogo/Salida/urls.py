from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import SalidaApiView
from .ModelViewSet import SalidaViewSet
from .models import Salida

router = DefaultRouter()
router.register(r'salida',SalidaViewSet, basename='salida')

urlpatterns = [

    path('', include(router.urls)),

]