from rest_framework.viewsets import ModelViewSet
from .Serializer import  DetalleEntrada
from App.Detalles.DetalleEntrada.Serializer import DetalleEntradaSerialize

class DetalleEntradaViewSet(ModelViewSet):
    queryset = DetalleEntrada.objects.all()
    serializer_class = DetalleEntradaSerialize
