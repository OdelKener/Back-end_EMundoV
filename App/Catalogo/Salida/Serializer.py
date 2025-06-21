from  rest_framework.serializers import  ModelSerializer

from App.Catalogo.Entrada.Serializer import EntradaSerialize
from  App.Catalogo.Salida.models import Salida
from . models import  *

class SalidaSerialize(ModelSerializer):
    class Meta:
        model = Salida
        fields = ['fechasalida','tiposalida','sucursalid_id','sucursalidhon_id','sucursalidcos_id','sucursalidpan_id',]

class DetalleSalidaSerialize(ModelSerializer):
    class Meta:
        model = DetalleSalida
        fields = ['salida_id','librohon_id','librocos_id','libropan_id','libro_id','cantidad','costosalida']

class SalidaDetalleSerialize(ModelSerializer):
    salida=SalidaSerialize()
    detallesalida=DetalleSalidaSerialize(many=True)
    class Meta:
        model= Salida
        fields = ['salida','detallesalida']