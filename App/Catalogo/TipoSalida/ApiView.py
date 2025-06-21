from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import TipoSalida
from .Serializer import TipoSalidaSerialize
from drf_yasg.utils import swagger_auto_schema

class TipoSalidaApiView(APIView):

    @swagger_auto_schema(responses={200: TipoSalidaSerialize(many=True)})
    def get(self, request):
        tiposalida = TipoSalida.objects.all()
        serializer = TipoSalida(tiposalida, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoSalidaSerialize, responses={201: TipoSalidaSerialize})
    def post(self, request):

        serializer = TipoSalidaSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoSalidaDetails(APIView):

    @swagger_auto_schema(responses={200:TipoSalidaSerialize})
    def get(self, request, pk):

        try:
            tiposalida=TipoSalida.objects.get(pk=pk)
        except TipoSalida.DoesNotExist:
            return  Response({'error': 'TipoSalida no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TipoSalidaSerialize(TipoSalida)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=TipoSalidaSerialize, responses={200: TipoSalidaSerialize})
    def put(self, request, pk ):

        try:
            tiposalida=TipoSalida.objects.get(pk=pk)
        except TipoSalida.DoesNotExist:
            return TipoSalida({'Error':'TipoSalida no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TipoSalidaSerialize(tiposalida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=TipoSalidaSerialize, responses={200: TipoSalidaSerialize})
    def delete(self, request, pk):

        try:
            tiposalida=TipoSalida.objects.get(pk=pk)
        except TipoSalida.DoesNotExist:
            return  Response({'Error': 'TipoSalida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer=TipoSalidaSerialize(tiposalida, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:TipoSalidaSerialize})
    def delete(self, request, pk):

        try:
            tiposalida=TipoSalida.objects.get(pk=pk)
        except TipoSalida.DoesNotExist:
            return Response({'Error': 'TipoSalida no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        tiposalida.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
