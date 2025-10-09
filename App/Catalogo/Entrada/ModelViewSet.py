from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction
from .models import Entrada, DetalleEntrada
from .Serializer import EntradaSerialize, DetalleEntradaSerialize

class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all().order_by('-id')
    serializer_class = EntradaSerialize
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                entrada = serializer.save()
                # Respuesta final con entrada y sus detalles
                return Response(
                    EntradaSerialize(entrada).data,
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class DetalleEntradaViewSet(viewsets.ModelViewSet):
    queryset = DetalleEntrada.objects.all()
    serializer_class = DetalleEntradaSerialize
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, 
            many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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



