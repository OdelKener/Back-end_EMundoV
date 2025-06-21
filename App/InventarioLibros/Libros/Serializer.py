from  rest_framework.serializers import  ModelSerializer
from  App.InventarioLibros.Libros.models import Libro

class LibrosSerialize(ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id','nombre', 'categorias_id', 'existencia', 'costoactual']