from django.contrib import admin

from Paises.Hondura.models import SucursalHon


@admin.register(SucursalHon)
class SucursalAdmin(admin.ModelAdmin):
    search_fields = ['codigo','nombre']
    list_display = ['codigo','nombre']
# Register your models here.
