from django.db import models

from App.Catalogo.TipoEntrada.models import TipoEntrada

from App.Paises.Nicaragua.models import Sucursal
from App.Paises.Panama.models import SucursalPan
from App.Paises.Hondura.models import SucursalHon
from App.Paises.CostaRica.models import SucursalCos

from App.InventarioLibros.Libros.models import Libro
from App.InventarioLibros.LibrosHon.models import LibrosHon
from App.InventarioLibros.LibrosCos.models import LibrosCos
from App.InventarioLibros.LibrosPan.models import LibrosPan


class Entrada(models.Model):
    fechaentrada = models.CharField(verbose_name='FechaEntrada', max_length=100)

    tipoentrada  = models.ForeignKey(TipoEntrada, verbose_name='TipoEntrada', on_delete=models.PROTECT,null=True, blank=True)

    sucursalid = models.ForeignKey(Sucursal,verbose_name='Sucursal', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidcos = models.ForeignKey(SucursalCos,verbose_name='SucursalCos', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidhon = models.ForeignKey(SucursalHon,verbose_name='SucursalHon', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidpan = models.ForeignKey(SucursalPan,verbose_name='SucursalPan', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Entradas'

    def __str__(self):
        return f'{self.tipoentrada}-{self.sucursalid}-{self.sucursalidhon}-{self.sucursalidcos}-{self.sucursalidpan}'

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
    return f'{self.entrada}-{self.libro}-{self.librocos}-{self.librohon}-{self.libropan}-{self.costoactual}-{self.cantidad}-'

class EntradaDetalle (models.Model):
    entrada =Entrada()
    detalleentrada= DetalleEntrada()

    class Meta:
        verbose_name= 'EntradasDetalles'

    def __str__(self):
            return f'{self.entrada}-{self.detalleentrada}'




# Create your models here.
# Create your models here.
