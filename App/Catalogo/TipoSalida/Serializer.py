from  rest_framework.serializers import  ModelSerializer
from  App.Catalogo.TipoSalida.models import TipoSalida

class TipoSalidaSerialize(ModelSerializer):
    class Meta:
        model = TipoSalida
        fields = ['id','nombre']