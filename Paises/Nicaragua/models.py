from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Sucursal(models.Model):
    nombre = models.CharField(max_length=255, default="Nicaragua", editable=False)
    codigo = models.IntegerField(default=1, editable=False)


    def __str__(self):
        return f"{self.nombre} - {self.codigo}"

    class Meta:
        verbose_name = "Sucursal"


@receiver(pre_save, sender=Sucursal)
def bloquear_modificacion_campos(sender, instance, **kwargs):
        if instance.pk:
            sucursal_antigua = Sucursal.objects.get(pk=instance.pk)
            instance.id = sucursal_antigua.id
            instance.nombre = sucursal_antigua.nombre

# Create your models here.
