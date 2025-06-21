from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import DetalleEntrada
from .Serializer import DetalleEntradaSerialize
from drf_yasg.utils import swagger_auto_schema

class DetalleEntradaApiView(APIView):

    @swagger_auto_schema(responses={200: DetalleEntradaSerialize(many=True)})
    def get(self, request):
        detalleentrada= DetalleEntrada.objects.all()
        serializer = DetalleEntrada(detalleentrada, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DetalleEntradaSerialize, responses={201: DetalleEntradaSerialize})
    def post(self, request):

        serializer = DetalleEntradaSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleEntradaDetails(APIView):

    @swagger_auto_schema(responses={200:DetalleEntradaSerialize})
    def get(self, request, pk):

        try:
            detalleentrada=DetalleEntradaSerialize.objects.get(pk=pk)
        except DetalleEntradaSerialize.DoesNotExist:
            return  Response({'error': 'DetalleEntrada no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetalleEntradaSerialize(DetalleEntradaSerialize)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=DetalleEntradaSerialize, responses={200: DetalleEntradaSerialize})
    def put(self, request, pk ):

        try:
            detalleentrada=DetalleEntradaSerialize.objects.get(pk=pk)
        except DetalleEntradaSerialize.DoesNotExist:
            return DetalleEntradaSerialize({'Error':'DetalleEntrada no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DetalleEntradaSerialize(detalleentrada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=DetalleEntradaSerialize, responses={200: DetalleEntradaSerialize})
    def delete(self, request, pk):

        try:
            detalleentrada=DetalleEntradaSerialize.objects.get(pk=pk)
        except DetalleEntradaSerialize.DoesNotExist:
            return  Response({'Error': 'DetalleEntrada no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer=DetalleEntradaSerialize(detalleentrada, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:DetalleEntradaSerialize})
    def delete(self, request, pk):

        try:
            detalleentrada=DetalleEntrada.objects.get(pk=pk)
        except DetalleEntrada.DoesNotExist:
            return Response({'Error': 'DetalleEntrada no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        detalleentrada.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
