from django.urls import path,include
from rest_framework.routers import  DefaultRouter
from .views import  CategoriaViewSet
from .ApiView import *


router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [

    path('', include(router.urls))

]

# app_name ="categoria"
#
# urlpatterns=[
#
#     path('',CategoriaApiView.as_view(), name="categoria"),
# ]