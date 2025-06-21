from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import LibrosCos
from .Serializer import LibrosCosSerialize
from drf_yasg.utils import swagger_auto_schema

class LibrosApiView(APIView):

    @swagger_auto_schema(responses={200: LibrosCosSerialize(many=True)})
    def get(self, request):

        libros = LibrosCos.objects.all()
        serializer = LibrosCos(libros, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LibrosCosSerialize, responses={201: LibrosCosSerialize})
    def post(self, request):

        serializer = LibrosCosSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibrosDetails(APIView):

    @swagger_auto_schema(responses={200:LibrosCosSerialize})
    def get(self, request, pk):

        try:
            Libros=LibrosCos.objects.get(pk=pk)
        except LibrosCos.DoesNotExist:
            return  Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrosCosSerialize(Libros)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=LibrosCosSerialize, responses={200: LibrosCosSerialize})
    def put(self, request, pk ):

        try:
            libros=LibrosCos.objects.get(pk=pk)
        except LibrosCos.DoesNotExist:
            return LibrosCos({'Error':'Libro no encontrad'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LibrosCosSerialize(libros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=LibrosCosSerialize, responses={200: LibrosCosSerialize})
    def delete(self, request, pk):

        try:
            libros=LibrosCos.objects.get(pk=pk)
        except LibrosCos.DoesNotExist:
            return  Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer=LibrosCosSerialize(libros, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:LibrosCosSerialize})
    def delete(self, request, pk):

        try:
            libros=LibrosCos.objects.get(pk=pk)
        except LibrosCos.DoesNotExist:
            return Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        libros.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
