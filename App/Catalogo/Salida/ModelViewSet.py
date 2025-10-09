from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction
from .models import Salida, DetalleSalida
from .Serializer import SalidaSerialize, DetalleSalidaSerialize


class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all().order_by('-id')
    serializer_class = SalidaSerialize
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=SalidaSerialize)
    def create(self, request, *args, **kwargs):
        serializer = SalidaSerialize(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Guardar la salida principal
                    salida = serializer.save()

                    # Guardar los detalles si vienen
                    detalles = request.data.get('detalles', [])
                    for det in detalles:
                        det['salida'] = salida.id
                        detalle_serializer = DetalleSalidaSerialize(data=det)
                        detalle_serializer.is_valid(raise_exception=True)
                        detalle_serializer.save()  # Aquí se resta la existencia automáticamente

                    # Respuesta final
                    response_data = {
                        "salida": SalidaSerialize(salida).data,
                        "detalles": DetalleSalidaSerialize(
                            DetalleSalida.objects.filter(salida=salida), many=True
                        ).data
                    }
                    return Response(response_data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalleSalidaViewSet(viewsets.ModelViewSet):
    queryset = DetalleSalida.objects.all()
    serializer_class = DetalleSalidaSerialize
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)






