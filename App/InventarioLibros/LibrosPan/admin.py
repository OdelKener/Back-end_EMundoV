from django.contrib import admin

from App.InventarioLibros.LibrosPan.models import LibrosPan
@admin.register(LibrosPan)
class LibroPanAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre','costoactual','existencia','categorias']