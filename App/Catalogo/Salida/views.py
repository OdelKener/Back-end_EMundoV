from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


from .models import *

from .Serializer import SalidaDetalleSerialize



class SalidaView( APIView):
    permission_classes = [IsAuthenticated]
    queryset = SalidaDetalle.objects.all()
    serializer_class = SalidaDetalleSerialize

# Create your views here.
