from  rest_framework.serializers import  ModelSerializer
from  App.Catalogo.TipoEntrada.models import TipoEntrada

class TipoEntradaSerialize(ModelSerializer):
    class Meta:
        model = TipoEntrada
        fields = ['id','nombre']