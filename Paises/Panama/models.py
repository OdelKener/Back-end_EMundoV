from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class SucursalPan(models.Model):
    nombre = models.CharField(max_length=255, default="Panama", editable=False)
    codigo = models.IntegerField(default=4, editable=False)


    def __str__(self):
        return f"{self.nombre} - {self.codigo}"

    class Meta:
        verbose_name = "SucursalPan"


@receiver(pre_save, sender=SucursalPan)
def bloquear_modificacion_campos(sender, instance, **kwargs):
        if instance.pk:
            sucursal_antigua = SucursalPan.objects.get(pk=instance.pk)
            instance.id = sucursal_antigua.id
            instance.nombre = sucursal_antigua.nombre

# Create your models here.
