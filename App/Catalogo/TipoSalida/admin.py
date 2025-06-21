from django.contrib import admin

from App.Catalogo.TipoSalida.models import TipoSalida


@admin.register(TipoSalida)
class TipoSalidaAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre']
# Register your models here.
