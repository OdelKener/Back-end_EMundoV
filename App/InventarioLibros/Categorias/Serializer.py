from rest_framework.serializers import ModelSerializer

from App.InventarioLibros.Categorias.models import Categoria

class CategoriaSerialaizer(ModelSerializer):
    class Meta:
     model = Categoria
     fields = ['id','nombre']


