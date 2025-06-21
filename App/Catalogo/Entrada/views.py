from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .ApiView import EntradaApiView
from .models import *
from .Serializer import EntradaSerialize
from .Serializer import EntradaDetalleSerialize



class EntradaView( APIView):
    permission_classes = [IsAuthenticated]
    queryset = EntradaDetalle.objects.all()
    serializer_class = EntradaDetalleSerialize

