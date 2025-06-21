from django.contrib import admin

from App.InventarioLibros.LibrosHon.models import LibrosHon
@admin.register(LibrosHon)
class LibroHonAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre','costoactual','existencia','categorias']