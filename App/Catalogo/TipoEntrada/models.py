from django.db import models




class TipoEntrada(models.Model):
    COMPRAS = 'compras'
    DEVOLUCION = 'devolucion'


    NOMBRE_CHOICES = [
        (COMPRAS, 'Compras'),
        (DEVOLUCION, 'Devolución'),

    ]

    nombre = models.CharField(
        verbose_name='Nombres',
        max_length=100,
        choices=NOMBRE_CHOICES,)


    class Meta:
        verbose_name = 'TiposEntradas'

    def __str__(self):
        return self.get_nombre_display()  # Muestra la opción legible

