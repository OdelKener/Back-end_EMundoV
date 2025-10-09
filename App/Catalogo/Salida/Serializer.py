from rest_framework import serializers
from App.Catalogo.Salida.models import Salida, DetalleSalida
from App.InventarioLibros.Libros.models import Libro

class DetalleSalidaSerialize(serializers.ModelSerializer):
    class Meta:
        model = DetalleSalida
        fields = ['salida', 'libro', 'librohon', 'librocos', 'libropan', 'cantidad', 'costosalida']

    def create(self, validated_data):
        detalle = super().create(validated_data)

        # CORREGIR: Usar 'libro' en lugar de 'libro_id'
        libro = None
        if detalle.libro:  # 'libro' es el objeto, no 'libro_id'
            libro = detalle.libro
        if libro:
            libro.existencia = (libro.existencia or 0) - detalle.cantidad
            # CORREGIR: No actualizar costoactual en salidas
            # libro.costoactual = detalle.costoactual  # Eliminar esta línea
            libro.save()
        return detalle

class SalidaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Salida
        fields = ['id',
            'fechasalida',
            'tiposalida_id',
            'sucursalid_id',
            'sucursalidhon_id',
            'sucursalidcos_id',
            'sucursalidpan_id',
        ]