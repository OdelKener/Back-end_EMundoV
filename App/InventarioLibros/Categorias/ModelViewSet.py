from rest_framework.viewsets import ModelViewSet
from .models import  Categoria
from .Serializer import  CategoriaSerialaizer
from rest_framework.permissions import AllowAny


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerialaizer
    permission_classes = [AllowAny]  # 🔑 permite acceso público