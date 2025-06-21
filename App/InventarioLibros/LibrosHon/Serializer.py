from  rest_framework.serializers import  ModelSerializer
from  App.InventarioLibros.LibrosHon.models import LibrosHon

class LibrosHonSerialize(ModelSerializer):
    class Meta:
        model = LibrosHon
        fields = ['id','nombre', 'categorias_id', 'existencia', 'costoactual']