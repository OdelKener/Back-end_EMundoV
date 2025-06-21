from django.contrib import admin

from App.InventarioLibros.Categorias.models import Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre']