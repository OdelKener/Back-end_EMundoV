from django.contrib import admin

from App.Paises.Nicaragua.models import Sucursal


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    search_fields = ['codigo','nombre']
    list_display = ['codigo','nombre']
# Register your models here.
