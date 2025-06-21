from django.contrib import admin

from App.Detalles.DetalleSalida.models import DetalleSalida


@admin.register(DetalleSalida)
class DetalleSalidaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id','costosalida','cantidad','salida','libro']

# Register your models here.
