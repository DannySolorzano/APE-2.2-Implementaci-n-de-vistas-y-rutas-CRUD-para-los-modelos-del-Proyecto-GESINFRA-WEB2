# calificaciones/management/commands/init_data.py
from django.core.management.base import BaseCommand
from calificaciones.models import Institucion, Docente, Estudiante, Pensum

class Command(BaseCommand):
    help = 'Inicializa datos de prueba para el módulo de calificaciones'
    
    def handle(self, *args, **kwargs):
        # Crear institución de prueba
        institucion, created = Institucion.objects.get_or_create(
            codigo_ame='INS001',
            defaults={
                'nombre': 'Institución Educativa Modelo',
                'direccion': 'Calle Principal #123',
                'sostenimiento': 'Público',
                'producto': 'Educación Media',
                'carton': 'Cartón Oficial',
                'correo': 'info@modelo.edu',
                'regimen_adaptivo': 'Regular'
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Institución creada'))
        
        # Crear docentes de prueba
        docentes_data = [
            {'codigo': 'DOC001', 'nombre': 'Ana', 'apellido': 'García', 'correo': 'ana@modelo.edu', 'comision': 'A'},
            {'codigo': 'DOC002', 'nombre': 'Carlos', 'apellido': 'Rodríguez', 'correo': 'carlos@modelo.edu', 'comision': 'B'},
        ]
        
        for docente_data in docentes_data:
            docente, created = Docente.objects.get_or_create(**docente_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Docente {docente.nombre} creado'))
        
        # Crear estudiantes de prueba
        estudiantes_data = [
            {'codigo': 'EST001', 'nombre': 'María', 'apellido': 'López', 'correo': 'maria@estudiante.edu'},
            {'codigo': 'EST002', 'nombre': 'Juan', 'apellido': 'Pérez', 'correo': 'juan@estudiante.edu'},
            {'codigo': 'EST003', 'nombre': 'Laura', 'apellido': 'Martínez', 'correo': 'laura@estudiante.edu'},
        ]
        
        for estudiante_data in estudiantes_data:
            estudiante, created = Estudiante.objects.get_or_create(**estudiante_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Estudiante {estudiante.nombre} creado'))
        
        self.stdout.write(self.style.SUCCESS('Datos de prueba inicializados correctamente'))