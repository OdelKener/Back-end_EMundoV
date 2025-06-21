from http.client import responses

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import LibrosHon
from .Serializer import LibrosHonSerialize
from drf_yasg.utils import swagger_auto_schema

class LibrosApiView(APIView):

    @swagger_auto_schema(responses={200: LibrosHonSerialize(many=True)})
    def get(self, request):

        libros =LibrosHon.objects.all()
        serializer =LibrosHon(libros, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LibrosHonSerialize, responses={201: LibrosHonSerialize})
    def post(self, request):

        serializer = LibrosHonSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LibrosDetails(APIView):

    @swagger_auto_schema(responses={200:LibrosHonSerialize})
    def get(self, request, pk):

        try:
            Libros=LibrosHon.objects.get(pk=pk)
        except LibrosHon.DoesNotExist:
            return  Response({'error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LibrosHonSerialize(Libros)
        return  Response(serializer.data)


    @swagger_auto_schema(request_body=LibrosHonSerialize, responses={200: LibrosHonSerialize})
    def put(self, request, pk ):

        try:
            libros=LibrosHon.objects.get(pk=pk)
        except LibrosHon.DoesNotExist:
            return LibrosHon({'Error':'Libro no encontrad'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LibrosHonSerialize(libros, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=LibrosHonSerialize, responses={200: LibrosHonSerialize})
    def delete(self, request, pk):

        try:
            libros=LibrosHon.objects.get(pk=pk)
        except LibrosHon.DoesNotExist:
            return  Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer=LibrosHonSerialize(libros, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(responses={200:LibrosHonSerialize})
    def delete(self, request, pk):

        try:
            libros=LibrosHon.objects.get(pk=pk)
        except LibrosHon.DoesNotExist:
            return Response({'Error': 'Libro no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        libros.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)
