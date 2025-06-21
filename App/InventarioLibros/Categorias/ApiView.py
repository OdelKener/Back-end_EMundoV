from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import  status
from .models import  Categoria
from .Serializer import CategoriaSerialaizer

class CategoriaApiView(APIView):

    def get(self, request, pk=None):

        if pk:
            try:
                categoria = Categoria.objects.get(pk=pk)
            except Categoria.DoesNotExist:
                return  Response({'Error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CategoriaSerialaizer(categoria)
            return Response(serializer.data)

        else:
            categoria = Categoria.objects.all()
            serializer = CategoriaSerialaizer(categoria, many=True)
            return Response(serializer.data)

        def post(self, request):

            serializer = CategoriaSerialaizer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def put(self, request, pk=None):
            try:
                categoria = Categoria.objects.get(pk=pk)
            except Categoria.DoesNotExist:
                return Response({'Error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CategoriaSerialaizer(categoria, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def patch(self, request, pk=None):

            try:
                categoria = Categoria.objects.get(pk=pk)
            except Categoria.DoesNotExist:
                return Response({'Error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CategoriaSerialaizer(categoria, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk=None):

            try:
                categoria = Categoria.objects.get(pk=pk)
            except Categoria.DoesNotExist:
                return Response({'Error': 'Categoria no encontrada'}, status=status.HTTP_404_NOT_FOUND)

            categoria.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
