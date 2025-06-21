from rest_framework.viewsets import ModelViewSet
from .models import  LibrosCos
from .Serializer import LibrosCosSerialize

class LibrosCosViewSet(ModelViewSet):
    queryset = LibrosCos.objects.all()
    serializer_class = LibrosCosSerialize
