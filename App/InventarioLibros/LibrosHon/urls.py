from django.urls import  path, include
from rest_framework.routers import  DefaultRouter


from .ApiView import LibrosApiView
from .ModelViewSet import LibrosHonViewSet
from .models import LibrosHon

router = DefaultRouter()
router.register(r'libros',LibrosHonViewSet, basename='libros')

urlpatterns = [

    path('', include(router.urls)),

]