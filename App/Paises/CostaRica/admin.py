from django.contrib import admin

from App.Paises.CostaRica.models import SucursalCos


@admin.register(SucursalCos)
class SucursalAdmin(admin.ModelAdmin):
    search_fields = ['codigo','nombre']
    list_display = ['codigo','nombre']
# Register your models here.
