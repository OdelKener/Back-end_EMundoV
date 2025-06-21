from django.db import models


from App.Catalogo.Entrada.models import Entrada
from App.InventarioLibros.Libros.models import Libro
from App.InventarioLibros.LibrosHon.models import LibrosHon
from App.InventarioLibros.LibrosCos.models import LibrosCos
from App.InventarioLibros.LibrosPan.models import LibrosPan




class DetalleEntrada(models.Model):


 costoactual = models.BigIntegerField(verbose_name='CostoActual', null=True, blank=True)
 cantidad= models.BigIntegerField(verbose_name='Cantidad', null=True, blank=True)
 entrada = models.ForeignKey(Entrada, verbose_name='Entrada', on_delete=models.PROTECT)
 libro = models.ForeignKey(Libro,verbose_name='Libro', on_delete=models.PROTECT,null=True, blank=True)
 librocos = models.ForeignKey(LibrosCos, verbose_name='LibroCos', on_delete=models.PROTECT, null=True, blank=True)
 librohon = models.ForeignKey(LibrosHon, verbose_name='LibroHon', on_delete=models.PROTECT, null=True, blank=True)
 libropan = models.ForeignKey(LibrosPan, verbose_name='LibroPan', on_delete=models.PROTECT, null=True, blank=True)


class Meta:
    verbose_name = 'DetallesEntradas'


def __str__(self):
    return f'{self.costoactual}-{self.cantidad}'

# Create your models here.
