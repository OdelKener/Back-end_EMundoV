from rest_framework.viewsets import ModelViewSet
from .models import  TipoEntrada
from .Serializer import TipoEntradaSerialize

class TipoEntradaViewSet(ModelViewSet):
    queryset = TipoEntrada.objects.all()
    serializer_class = TipoEntradaSerialize
