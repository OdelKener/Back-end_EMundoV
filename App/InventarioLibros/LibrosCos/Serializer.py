from  rest_framework.serializers import  ModelSerializer
from  App.InventarioLibros.LibrosCos.models import LibrosCos

class LibrosCosSerialize(ModelSerializer):
    class Meta:
        model = LibrosCos
        fields = ['id','nombre', 'categorias_id', 'existencia', 'costoactual']