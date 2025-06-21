from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import TipoEntrada
from .Serializer import TipoEntradaSerialize
from drf_yasg.utils import swagger_auto_schema

class TipoEntradaApiView(APIView):

    @swagger_auto_schema(responses={200: TipoEntradaSerialize(many=True)})
    def get(self, request):
        tipoentrada = TipoEntrada.objects.all()
        serializer = TipoEntrada(tipoentrada, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoEntradaSerialize, responses={201: TipoEntradaSerialize})
    def post(self, request):

        serializer = TipoEntradaSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoEntradaDetails(APIView):

    @swagger_auto_schema(responses={200:TipoEntradaSerialize})
    def get(self, request, pk):

        try:
            tipoentrada=TipoEntrada.objects.get(pk=pk)
        except TipoEntrada.DoesNotExist:
            return  Response({'error': 'TipoEntrada no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TipoEntradaSerialize(TipoEntrada)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=TipoEntradaSerialize, responses={200: TipoEntradaSerialize})
    def put(self, request, pk ):

        try:
            tipoentrada=TipoEntrada.objects.get(pk=pk)
        except TipoEntrada.DoesNotExist:
            return TipoEntrada({'Error':'TipoEntrada no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TipoEntradaSerialize(tipoentrada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=TipoEntradaSerialize, responses={200: TipoEntradaSerialize})
    def delete(self, request, pk):

        try:
            tipoentrada=TipoEntrada.objects.get(pk=pk)
        except TipoEntrada.DoesNotExist:
            return  Response({'Error': 'TipoEntrada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer=TipoEntradaSerialize(tipoentrada, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:TipoEntradaSerialize})
    def delete(self, request, pk):

        try:
            tipoentrada=TipoEntrada.objects.get(pk=pk)
        except TipoEntrada.DoesNotExist:
            return Response({'Error': 'TipoEntrada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        tipoentrada.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
