from django.contrib import admin

from App.Catalogo.Entrada.models import Entrada


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id','fechaentrada','tipoentrada']
# Register your models here.
