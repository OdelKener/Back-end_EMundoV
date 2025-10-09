from rest_framework.viewsets import ModelViewSet
from .models import  TipoSalida
from .Serializer import TipoSalidaSerialize
from rest_framework.permissions import AllowAny


class TipoSalidaViewSet(ModelViewSet):
    queryset = TipoSalida.objects.all()
    serializer_class = TipoSalidaSerialize
    permission_classes = [AllowAny]  # 🔑 permite acceso público
    
