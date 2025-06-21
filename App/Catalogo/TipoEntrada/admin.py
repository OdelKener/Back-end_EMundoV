from django.contrib import admin

from App.Catalogo.TipoEntrada.models import TipoEntrada


@admin.register(TipoEntrada)
class TipoEntradaAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre']
# Register your models here.
