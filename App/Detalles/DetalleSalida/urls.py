from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import DetalleSalidaApiView
from .ModelViewSet import DetalleSalidaViewSet
from .models import DetalleSalida

router = DefaultRouter()
router.register(r'detallesalida',DetalleSalidaViewSet, basename='detallesalida')

urlpatterns = [

    path('', include(router.urls)),

]