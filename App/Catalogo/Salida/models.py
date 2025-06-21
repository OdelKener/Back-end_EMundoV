from django.db import models

from App.Catalogo.TipoSalida.models import TipoSalida
from App.Paises.Nicaragua.models import Sucursal
from App.Paises.Panama.models import SucursalPan
from App.Paises.Hondura.models import SucursalHon
from App.Paises.CostaRica.models import SucursalCos
from App.InventarioLibros.Libros.models import Libro
from App.InventarioLibros.LibrosHon.models import LibrosHon
from App.InventarioLibros.LibrosCos.models import LibrosCos
from App.InventarioLibros.LibrosPan.models import LibrosPan


class Salida(models.Model):
    fechasalida = models.CharField(verbose_name='FechaSalida', max_length=100)

    tiposalida= models.ForeignKey(TipoSalida, verbose_name='TipoSalida', on_delete=models.PROTECT, null=True, blank=True)

    sucursalid = models.ForeignKey(Sucursal, verbose_name='Sucursal', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidcos = models.ForeignKey(SucursalCos, verbose_name='Sucursalcos', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidhon = models.ForeignKey(SucursalHon, verbose_name='SucursalHon', on_delete=models.PROTECT, null=True, blank=True)
    sucursalidpan = models.ForeignKey(SucursalPan, verbose_name='SucursalPan', on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
     verbose_name = 'Salidas'

    def __str__(self):
     return f'{self.tiposalida}-{self.fechasalida}-{self.sucursalid}-{self.sucursalidcos}-{self.sucursalidhon}-{self.sucursalidpan}'

class DetalleSalida(models.Model):
 costosalida = models.BigIntegerField(verbose_name='CostoSalida', null=True, blank=True)
 cantidad = models.BigIntegerField(verbose_name='Cantidad', null=True, blank=True)
 salida = models.ForeignKey(Salida, verbose_name='Salida', on_delete=models.PROTECT)
 libro = models.ForeignKey(Libro, verbose_name='Libro', on_delete=models.PROTECT, null=True, blank=True)
 librocos = models.ForeignKey(LibrosCos, verbose_name='LibroCos', on_delete=models.PROTECT, null=True, blank=True)
 librohon = models.ForeignKey(LibrosHon, verbose_name='LibroHon', on_delete=models.PROTECT, null=True, blank=True)
 libropan = models.ForeignKey(LibrosPan, verbose_name='LibroPan', on_delete=models.PROTECT, null=True, blank=True)


 class Meta:
  verbose_name = 'DetallesSalidas'

 def __str__(self):
     return f'{self.salida}-{self.libro}-{self.librocos}-{self.librohon}-{self.libropan}{self.costosalida},{self.cantidad}'


class SalidaDetalle (models.Model):
    salida =Salida()
    detallesalida=DetalleSalida()


    class Meta:
        verbose_name = 'SalidasDetalles'

    def __str__(self):
            return f'{self.salida}-{self.detallesalida}'

# Create your models here.
