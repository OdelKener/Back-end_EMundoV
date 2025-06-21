from  rest_framework.serializers import  ModelSerializer
from  App.Detalles.DetalleEntrada.models import DetalleEntrada

class DetalleEntradaSerialize(ModelSerializer):
    class Meta:
        model = DetalleEntrada
        fields = ['entrada_id','libro_id','cantidad','costoactual']