from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import TipoSalidaApiView
from .ModelViewSet import TipoSalidaViewSet
from .models import TipoSalida

router = DefaultRouter()
router.register(r'tiposalida',TipoSalidaViewSet, basename='tiposalida')

urlpatterns = [

    path('', include(router.urls)),

]