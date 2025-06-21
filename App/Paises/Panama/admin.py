from django.contrib import admin

from App.Paises.Panama.models import SucursalPan


@admin.register(SucursalPan)
class SucursalAdmin(admin.ModelAdmin):
    search_fields = ['codigo','nombre']
    list_display = ['codigo','nombre']
# Register your models here.
