from django.contrib import admin

from App.Detalles.DetalleEntrada.models import DetalleEntrada


@admin.register(DetalleEntrada)
class DetalleEntradaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id','costoactual','cantidad','entrada','libro']
# Register your models here.
