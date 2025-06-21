from django.contrib import admin

from App.InventarioLibros.Libros.models import Libro
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['id','nombre','costoactual','existencia','categorias']