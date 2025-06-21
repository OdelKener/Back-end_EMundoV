from rest_framework.viewsets import ModelViewSet
from .models import  Libro
from .Serializer import LibrosSerialize

class LibrosViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibrosSerialize
