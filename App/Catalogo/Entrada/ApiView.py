from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import Entrada
from .Serializer import EntradaSerialize
from drf_yasg.utils import swagger_auto_schema

class EntradaApiView(APIView):

    @swagger_auto_schema(responses={200: EntradaSerialize(many=True)})
    def get(self, request):

        entrada = Entrada.objects.all()
        serializer = EntradaSerialize(entrada, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EntradaSerialize, responses={201: EntradaSerialize})
    def post(self, request):

        serializer = EntradaSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EntradaDetails(APIView):

    @swagger_auto_schema(responses={200:EntradaSerialize})
    def get(self, request, pk):

        try:
            entrada=Entrada.objects.get(pk=pk)
        except Entrada.DoesNotExist:
            return  Response({'error': 'Entrada no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EntradaSerialize(entrada)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=EntradaSerialize, responses={200: EntradaSerialize})
    def put(self, request, pk ):

        try:
            entrada=Entrada.objects.get(pk=pk)
        except Entrada.DoesNotExist:
            return Entrada({'Error':'Entrada no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EntradaSerialize(entrada, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=EntradaSerialize, responses={200: EntradaSerialize})
    def delete(self, request, pk):

        try:
            entrada=Entrada.objects.get(pk=pk)
        except Entrada.DoesNotExist:
            return  Response({'Error': 'Entrada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer=EntradaSerialize(entrada, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:EntradaSerialize})
    def delete(self, request, pk):

        try:
            entrada=Entrada.objects.get(pk=pk)
        except Entrada.DoesNotExist:
            return Response({'Error': 'Entrada no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        entrada.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
