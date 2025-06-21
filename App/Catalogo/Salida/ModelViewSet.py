from rest_framework.viewsets import ModelViewSet
from .models import  Salida
from .Serializer import SalidaSerialize, SalidaDetalleSerialize

from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from .Serializer import *

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all()
    serializer_class = SalidaDetalleSerialize()

    @swagger_auto_schema(request_body=SalidaDetalleSerialize)
    def create(self, request, *args, **kwargs):
        serializer = SalidaDetalleSerialize(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Guarda la entrada
                    salida_data = serializer.validated_data['salida']
                    salida = Salida.objects.create(**salida_data)

                    # Guarda cada detalle asociado
                    detalles_data = serializer.validated_data['detallesalida']
                    for detalle_data in detalles_data:
                        detalle_data['salida'] = salida  # Asocia el detalle a la entrada creada
                        DetalleSalida.objects.create(**detalle_data)

                    # Responde con los datos creados
                    response_data = {
                        "salida": SalidaSerialize(salida).data,
                        "detallesalida": DetalleSalidaSerialize(DetalleSalida.objects.filter(salida=salida),
                                                                  many=True).data
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





