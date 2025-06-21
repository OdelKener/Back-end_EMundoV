from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from .models import  Entrada
from .Serializer import *

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import *

from rest_framework.response import Response


class EntradaViewSet(viewsets.ModelViewSet):
   queryset = Entrada.objects.all()
   serializer_class = EntradaDetalleSerialize()

   @swagger_auto_schema(request_body=EntradaDetalleSerialize)
   def create(self, request, *args, **kwargs):
      serializer = EntradaDetalleSerialize(data=request.data)

      if serializer.is_valid():
         try:
            with transaction.atomic():
               # Guarda la entrada
               entrada_data = serializer.validated_data['entrada']
               entrada = Entrada.objects.create(**entrada_data)

               # Guarda cada detalle asociado
               detalles_data = serializer.validated_data['detalleentrada']
               for detalle_data in detalles_data:
                  detalle_data['entrada'] = entrada  # Asocia el detalle a la entrada creada
                  DetalleEntrada.objects.create(**detalle_data)

               # Responde con los datos creados
               response_data = {
                  "entrada": EntradaSerialize(entrada).data,
                  "detalleentrada": DetalleEntradaSerialize(DetalleEntrada.objects.filter(entrada=entrada),
                                                            many=True).data
               }
               return Response(response_data, status=status.HTTP_201_CREATED)

         except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



 #   queryset = EntradaDetalle.objects.all()
 #   serializer_class = EntradaDetalleSerialize
 #
 #
 # @swagger_auto_schema(request_body=EntradaDetalleSerialize)
 #
 # def post(self, request):
 #
 #  entradadetalle_serializer = EntradaDetalleSerialize(data=request.data)
 #
 #  if EntradaDetalleSerialize.is_valid():
 #     try:
 #        with transaction.atomic():
 #
 #           entrada = EntradaDetalleSerialize.save()
 #
 #
 #           detalles_data = request.data.get('detalles', [])
 #           for detalle_data in detalles_data:
 #              detalle_data['entrada'] = entrada.id  # Asociar cada detalle con la entrada creada
 #              detalle_serializer = EntradaDetalleSerialize(data=detalle_data)
 #
 #              # Validar cada DetalleEntrada
 #              if detalle_serializer.is_valid():
 #                 detalle_serializer.save()
 #              else:
 #                 return Response(detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 #
 #           # Responder con los datos creados
 #           response_data = {
 #              "entrada": EntradaDetalleSerialize.data,
 #              "detalles": EntradaDetalleSerialize(DetalleEntrada.objects.filter(entrada=entrada), many=True).data
 #           }
 #           return Response(response_data, status=status.HTTP_201_CREATED)
 #
 #     except Exception as e:
 #        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
 #
 #  return Response(EntradaDetalleSerialize.errors, status=status.HTTP_400_BAD_REQUEST)



