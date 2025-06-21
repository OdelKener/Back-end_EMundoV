from rest_framework.viewsets import ModelViewSet
from .models import  LibrosPan
from .Serializer import LibrosPanSerialize

class LibrosPanViewSet(ModelViewSet):
    queryset = LibrosPan.objects.all()
    serializer_class = LibrosPanSerialize
