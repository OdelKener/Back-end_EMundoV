from rest_framework import serializers
from .models import Entrada, DetalleEntrada
from App.InventarioLibros.Libros.models import Libro

class DetalleEntradaSerialize(serializers.ModelSerializer):
    class Meta:
        model = DetalleEntrada
        # CORREGIR: Usar los nombres correctos del modelo
        fields = ['entrada', 'libro', 'librohon', 'librocos', 'libropan', 'cantidad', 'costoactual']

    def create(self, validated_data):
        detalle = super().create(validated_data)

        # CORREGIR: Usar 'libro' en lugar de 'libro_id'
        libro = None
        if detalle.libro:  # 'libro' es el objeto, no 'libro_id'
            libro = detalle.libro
        if libro:
            libro.existencia = (libro.existencia or 0) + detalle.cantidad
            libro.costoactual = detalle.costoactual
            libro.save()
        return detalle

class EntradaSerialize(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = [
            'id',
            'fechaentrada',
            'tipoentrada_id',
            'sucursalid_id',
            'sucursalidhon_id',
            'sucursalidcos_id',
            'sucursalidpan_id',
        ]
        read_only_fields = ['id']