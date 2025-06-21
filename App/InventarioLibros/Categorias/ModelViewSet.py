from rest_framework.viewsets import ModelViewSet
from .models import  Categoria
from .Serializer import  CategoriaSerialaizer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerialaizer
