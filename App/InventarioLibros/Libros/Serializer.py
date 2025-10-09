from  rest_framework.serializers import  ModelSerializer
from  App.InventarioLibros.Libros.models import Libro


class LibrosSerialize(ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id','nombre', 'categorias', 'existencia', 'costoactual']
        
    def validate_categoria(self, value):
        if value is None:
            raise ModelSerializer.ValidationError("Debe seleccionar una categoría válida.")
        return value