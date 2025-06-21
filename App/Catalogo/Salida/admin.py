from django.contrib import admin

from App.Catalogo.Salida.models import Salida


@admin.register(Salida)
class SalidaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id','fechasalida','tiposalida']
# Register your models here.
