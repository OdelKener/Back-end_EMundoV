from rest_framework.viewsets import ModelViewSet
from .Serializer import  DetalleSalida
from App.Detalles.DetalleSalida.Serializer import DetalleSalidaSerialize

class DetalleSalidaViewSet(ModelViewSet):
    queryset = DetalleSalida.objects.all()
    serializer_class = DetalleSalidaSerialize
