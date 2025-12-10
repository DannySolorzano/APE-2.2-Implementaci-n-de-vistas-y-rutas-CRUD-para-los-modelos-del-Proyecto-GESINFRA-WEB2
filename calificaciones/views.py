from django.shortcuts import render
from .models import Calificacion, Estudiante, Docente, Institucion

def index(request):
    total_calificaciones = Calificacion.objects.count()
    total_estudiantes = Estudiante.objects.count()
    total_docentes = Docente.objects.count()
    total_instituciones = Institucion.objects.count()
    
    context = {
        'total_calificaciones': total_calificaciones,
        'total_estudiantes': total_estudiantes,
        'total_docentes': total_docentes,
        'total_instituciones': total_instituciones,
        'titulo': 'Sistema de Calificaciones'
    }
    return render(request, 'calificaciones/index.html', context)