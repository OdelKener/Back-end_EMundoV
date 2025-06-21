from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import Libro
from .Serializer import LibrosSerialize
from drf_yasg.utils import swagger_auto_schema

class LibrosApiView(APIView):

    @swagger_auto_schema(responses={200: LibrosSerialize(many=True)})
    def get(self, request):

        libros = Libro.objects.all()
        serializer = Libro(libros, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LibrosSerialize, responses={201: LibrosSerialize})
    def post(self, request):

        serializer = LibrosSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibrosDetails(APIView):

    @swagger_auto_schema(responses={200:LibrosSerialize})
    def get(self, request, pk):

        try:
            Libros=Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return  Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrosSerialize(Libros)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=LibrosSerialize, responses={200: LibrosSerialize})
    def put(self, request, pk ):

        try:
            libros=Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return Libro({'Error':'Libro no encontrad'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LibrosSerialize(libros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=LibrosSerialize, responses={200: LibrosSerialize})
    def delete(self, request, pk):

        try:
            libros=Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return  Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer=LibrosSerialize(libros, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:LibrosSerialize})
    def delete(self, request, pk):

        try:
            libros=Libro.objects.get(pk=pk)
        except Libro.DoesNotExist:
            return Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        libros.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
