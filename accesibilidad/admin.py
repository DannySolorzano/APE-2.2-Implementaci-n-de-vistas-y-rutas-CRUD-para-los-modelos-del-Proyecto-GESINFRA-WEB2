from django.contrib import admin
from .models import *

@admin.register(ConfiguracionAccesibilidad)
class ConfiguracionAccesibilidadAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'alto_contraste', 'tamanio_fuente', 'lectura_asistida', 'ultima_actualizacion')
    list_filter = ('alto_contraste', 'tamanio_fuente', 'lectura_asistida')
    search_fields = ('usuario__username', 'token_accesibilidad')

@admin.register(TerminologiaEspecifica)
class TerminologiaEspecificaAdmin(admin.ModelAdmin):
    list_display = ('termino', 'categoria', 'activo', 'fecha_creacion')
    list_filter = ('categoria', 'activo')
    search_fields = ('termino', 'definicion')

@admin.register(ControlTransicionesTexto)
class ControlTransicionesTextoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'efecto', 'activo')
    list_filter = ('efecto', 'activo')
    search_fields = ('nombre',)

@admin.register(TokenInmunizacion)
class TokenInmunizacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha_expiracion', 'activo', 'fecha_creacion')
    list_filter = ('tipo', 'activo')
    search_fields = ('nombre', 'valor')
    
    def esta_expirado(self, obj):
        return obj.esta_expirado()
    esta_expirado.boolean = True
    esta_expirado.short_description = 'Expirado'

@admin.register(ContenidoAccesible)
class ContenidoAccesibleAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'replicado', 'fecha_creacion', 'ultima_replicacion')
    list_filter = ('tipo', 'replicado')
    search_fields = ('titulo', 'contenido')
    readonly_fields = ('ultima_replicacion',)

@admin.register(RecursoAccesible)
class RecursoAccesibleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'activo', 'almacenamiento_recurrente', 'fecha_creacion')
    list_filter = ('tipo', 'activo', 'almacenamiento_recurrente')
    search_fields = ('nombre', 'descripcion', 'descriptor')
    filter_horizontal = ()

@admin.register(FiltroRecurso)
class FiltroRecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'tipo_filtro', 'valor', 'prioridad')
    list_filter = ('tipo_filtro',)
    search_fields = ('valor', 'recurso__nombre')

@admin.register(LogAccesibilidad)
class LogAccesibilidadAdmin(admin.ModelAdmin):
    list_display = ('tipo_accion', 'usuario', 'fecha', 'descripcion')
    list_filter = ('tipo_accion', 'fecha')
    search_fields = ('descripcion', 'usuario__username')
    readonly_fields = ('fecha', 'datos')
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False