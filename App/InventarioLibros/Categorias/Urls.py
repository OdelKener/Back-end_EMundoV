from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from .ModelViewSet import  CategoriaViewSet
from .ApiView import *


router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [

    path('', include(router.urls))

]

