from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import DetalleSalida
from .Serializer import DetalleSalidaSerialize
from drf_yasg.utils import swagger_auto_schema

class DetalleSalidaApiView(APIView):

    @swagger_auto_schema(responses={200: DetalleSalidaSerialize(many=True)})
    def get(self, request):
        detallesalida= DetalleSalida.objects.all()
        serializer = DetalleSalida(detallesalida, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DetalleSalidaSerialize, responses={201: DetalleSalidaSerialize})
    def post(self, request):

        serializer = DetalleSalidaSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleSalidaDetails(APIView):

    @swagger_auto_schema(responses={200:DetalleSalidaSerialize})
    def get(self, request, pk):

        try:
            detallesalida=DetalleSalidaSerialize.objects.get(pk=pk)
        except DetalleSalidaSerialize.DoesNotExist:
            return  Response({'error': 'DetalleSalida no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetalleSalidaSerialize(DetalleSalidaSerialize)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=DetalleSalidaSerialize, responses={200: DetalleSalidaSerialize})
    def put(self, request, pk ):

        try:
            detallesalida=DetalleSalidaSerialize.objects.get(pk=pk)
        except DetalleSalidaSerialize.DoesNotExist:
            return DetalleSalidaSerialize({'Error':'DetalleSalida no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DetalleSalidaSerialize(detallesalida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=DetalleSalidaSerialize, responses={200: DetalleSalidaSerialize})
    def delete(self, request, pk):

        try:
            detallesalida=DetalleSalidaSerialize.objects.get(pk=pk)
        except DetalleSalidaSerialize.DoesNotExist:
            return  Response({'Error': 'DetalleSalida no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer=DetalleSalidaSerialize(detallesalida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:DetalleSalidaSerialize})
    def delete(self, request, pk):

        try:
            detallesalida=DetalleSalida.objects.get(pk=pk)
        except DetalleSalida.DoesNotExist:
            return Response({'Error': 'DetalleSalida no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detallesalida.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
