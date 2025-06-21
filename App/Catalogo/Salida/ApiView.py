from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import Salida
from .Serializer import SalidaSerialize
from drf_yasg.utils import swagger_auto_schema

class SalidaApiView(APIView):

    @swagger_auto_schema(responses={200: SalidaSerialize(many=True)})
    def get(self, request):
        salida = Salida.objects.all()
        serializer = salida(salida, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SalidaSerialize, responses={201: SalidaSerialize})
    def post(self, request):

        serializer = SalidaSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalidaDetails(APIView):

    @swagger_auto_schema(responses={200:SalidaSerialize})
    def get(self, request, pk):

        try:
            salida=Salida.objects.get(pk=pk)
        except Salida.DoesNotExist:
            return  Response({'error': 'Salida no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SalidaSerialize(Salida)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=SalidaSerialize, responses={200: SalidaSerialize})
    def put(self, request, pk ):

        try:
            salida=Salida.objects.get(pk=pk)
        except Salida.DoesNotExist:
            return Salida({'Error':'Salida no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SalidaSerialize(salida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=SalidaSerialize, responses={200: SalidaSerialize})
    def delete(self, request, pk):

        try:
            salida=Salida.objects.get(pk=pk)
        except Salida.DoesNotExist:
            return  Response({'Error': 'Salida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer=SalidaSerialize(salida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:SalidaSerialize})
    def delete(self, request, pk):

        try:
            salida=Salida.objects.get(pk=pk)
        except Salida.DoesNotExist:
            return Response({'Error': 'Salida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        salida.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
