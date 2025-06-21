from  rest_framework.serializers import  ModelSerializer
from  App.Catalogo.Entrada.models import Entrada
from .models import *

class EntradaSerialize(ModelSerializer):
    class Meta:
        model = Entrada
        fields = [ 'fechaentrada','tipoentrada_id','sucursalid_id','sucursalidhon_id','sucursalidcos_id','sucursalidpan_id',]

class DetalleEntradaSerialize(ModelSerializer):
    class Meta:
        model = DetalleEntrada
        fields = ['entrada_id','libro_id','librohon_id','librocos_id','libropan_id','cantidad','costoactual']

class EntradaDetalleSerialize(ModelSerializer):
    entrada=EntradaSerialize()
    detalleentrada=DetalleEntradaSerialize(many=True)
    class Meta:
        model = Entrada
        fields =['entrada','detalleentrada']
