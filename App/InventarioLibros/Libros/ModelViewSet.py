from rest_framework.viewsets import ModelViewSet
from .models import  Libro
from .Serializer import LibrosSerialize
from rest_framework.permissions import AllowAny

class LibrosViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibrosSerialize
    permission_classes = [AllowAny]  # 🔑 permite acceso público
