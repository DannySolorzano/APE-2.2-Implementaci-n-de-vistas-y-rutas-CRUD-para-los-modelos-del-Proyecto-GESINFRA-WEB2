# calificaciones/admin.py
from django.contrib import admin
from .models import *

admin.site.register(Institucion)
admin.site.register(Docente)
admin.site.register(NivelEducativo)
admin.site.register(Estudiante)
admin.site.register(Paralelo)
admin.site.register(Directivo)
admin.site.register(Calificacion)