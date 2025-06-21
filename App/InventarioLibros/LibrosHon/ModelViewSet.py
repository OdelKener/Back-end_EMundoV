from rest_framework.viewsets import ModelViewSet
from .models import  LibrosHon
from .Serializer import LibrosHonSerialize

class LibrosHonViewSet(ModelViewSet):
    queryset = LibrosHon.objects.all()
    serializer_class = LibrosHonSerialize
