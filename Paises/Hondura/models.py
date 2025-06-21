from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class SucursalHon(models.Model):
    nombre = models.CharField(max_length=255, default="Hondura", editable=False)
    codigo = models.IntegerField(default=2, editable=False)


    def __str__(self):
        return f"{self.nombre} - {self.codigo}"

    class Meta:
        verbose_name = "SucursalHon"


@receiver(pre_save, sender=SucursalHon)
def bloquear_modificacion_campos(sender, instance, **kwargs):
        if instance.pk:
            sucursal_antigua = SucursalHon.objects.get(pk=instance.pk)
            instance.id = sucursal_antigua.id
            instance.nombre = sucursal_antigua.nombre

# Create your models here.
