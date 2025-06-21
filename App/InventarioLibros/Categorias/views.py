from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework.viewsets import  ModelViewSet
from .models import Categoria
from .Serializer import CategoriaSerialaizer

class CategoriaViewSet( ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerialaizer
#     def get(self, request):
#         serialize=CategoriaSerialaizer(Categoria.objects.all(), many=True)
#         # categoria=list(Categoria.objects.values())
#         return  Response(status=status.HTTP_200_OK, data=serialize.data)
#         # return Response({'categoria':Categoria.objects.all()})


# Create your views here.
