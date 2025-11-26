# accesibilidad/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(ModuloAccesibilidad)
admin.site.register(ConfiguracionAccesibilidad)
admin.site.register(ControlContraste)
admin.site.register(ControlTamañoTexto)
admin.site.register(RecursosInclusion)