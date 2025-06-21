from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import LibrosPan
from .Serializer import LibrosPanSerialize
from drf_yasg.utils import swagger_auto_schema

class LibrosPanApiView(APIView):

    @swagger_auto_schema(responses={200: LibrosPanSerialize(many=True)})
    def get(self, request):

        libros =LibrosPan.objects.all()
        serializer =LibrosPan(libros, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LibrosPanSerialize, responses={201: LibrosPanSerialize})
    def post(self, request):

        serializer = LibrosPanSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibrosPanDetails(APIView):

    @swagger_auto_schema(responses={200:LibrosPanSerialize})
    def get(self, request, pk):

        try:
            Libros=LibrosPan.objects.get(pk=pk)
        except LibrosPan.DoesNotExist:
            return  Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrosPanSerialize(Libros)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=LibrosPanSerialize, responses={200: LibrosPanSerialize})
    def put(self, request, pk ):

        try:
            libros=LibrosPan.objects.get(pk=pk)
        except LibrosPan.DoesNotExist:
            return LibrosPan({'Error':'Libro no encontrad'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LibrosPanSerialize(libros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=LibrosPanSerialize, responses={200: LibrosPanSerialize})
    def delete(self, request, pk):

        try:
            libros=LibrosPan.objects.get(pk=pk)
        except LibrosPan.DoesNotExist:
            return  Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer=LibrosPanSerialize(libros, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:LibrosPanSerialize})
    def delete(self, request, pk):

        try:
            libros=LibrosPan.objects.get(pk=pk)
        except LibrosPan.DoesNotExist:
            return Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        libros.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
