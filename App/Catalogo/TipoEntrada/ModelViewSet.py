from rest_framework.viewsets import ModelViewSet
from .models import  TipoEntrada
from .Serializer import TipoEntradaSerialize
from rest_framework.permissions import AllowAny

class TipoEntradaViewSet(ModelViewSet):
    queryset = TipoEntrada.objects.all()
    serializer_class = TipoEntradaSerialize
    permission_classes = [AllowAny]  # 🔑 permite acceso público
    
