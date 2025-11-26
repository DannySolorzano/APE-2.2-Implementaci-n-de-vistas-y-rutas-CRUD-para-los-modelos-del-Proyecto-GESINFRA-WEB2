# inventario/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Equipo)
admin.site.register(TipoEquipo)
admin.site.register(EstadoEquipo)
admin.site.register(Ubicacion)
admin.site.register(Responsable)
admin.site.register(Proveedor)