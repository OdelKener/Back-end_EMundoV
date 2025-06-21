from  rest_framework.serializers import  ModelSerializer
from  App.Detalles.DetalleSalida.models import DetalleSalida

class DetalleSalidaSerialize(ModelSerializer):
    class Meta:
        model = DetalleSalida
        fields = ['id','salida_id','libro_id','cantidad','costosalida']