from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(verbose_name='Nombre',max_length=100)
    class Meta:
        verbose_name = 'Categorias'

    def __str__(self):
        return f'{self.nombre}'

# Create your models here.
