from rest_framework.viewsets import ModelViewSet
from .models import  TipoSalida
from .Serializer import TipoSalidaSerialize

class TipoSalidaViewSet(ModelViewSet):
    queryset = TipoSalida.objects.all()
    serializer_class = TipoSalidaSerialize
