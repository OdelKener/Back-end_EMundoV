from  rest_framework.serializers import  ModelSerializer
from  App.InventarioLibros.LibrosPan.models import LibrosPan

class LibrosPanSerialize(ModelSerializer):
    class Meta:
        model = LibrosPan
        fields = ['id','nombre', 'categorias_id', 'existencia', 'costoactual']