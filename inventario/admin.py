from django.contrib import admin
from .models import Equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('numero_inventario', 'descripcion', 'precio_adquisicion', 'responsable', 'fecha_registro', 'activo')
    list_filter = ('activo', 'responsable', 'fecha_registro')
    search_fields = ('numero_inventario', 'descripcion')
    ordering = ('-fecha_registro',)

# Register your models here.
