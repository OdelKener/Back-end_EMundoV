from django.contrib import admin

from App.InventarioLibros.LibrosCos.models import LibrosCos
@admin.register(LibrosCos)
class LibroCosAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre','costoactual','existencia','categorias']