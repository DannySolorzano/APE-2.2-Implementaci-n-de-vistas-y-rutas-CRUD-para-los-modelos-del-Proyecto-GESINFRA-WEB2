# accesibilidad/models.py
from django.db import models

class Usuario(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ModuloAccesibilidad(models.Model):
    titulo = models.CharField(max_length=100)
    id_modulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class ConfiguracionAccesibilidad(models.Model):
    contraste_alto = models.BooleanField(default=False)
    tamaño_texto = models.CharField(max_length=20)
    lector_activado = models.BooleanField(default=False)

    def activar_contraste_alto(self):
        self.contraste_alto = True
        self.save()

    def cambiar_tamaño_texto(self, nuevo_tamaño):
        self.tamaño_texto = nuevo_tamaño
        self.save()

    def activar_lector(self):
        self.lector_activado = True
        self.save()

    def __str__(self):
        return "Configuración Accesibilidad"

class ControlContraste(models.Model):
    contraste_activado = models.BooleanField(default=False)

    def replicar_contraste_alto(self):
        # Lógica para replicar configuración
        pass

    def restaurar_contraste(self):
        self.contraste_activado = False
        self.save()

    def __str__(self):
        return f"Contraste: {'Activado' if self.contraste_activado else 'Desactivado'}"

class ControlTamañoTexto(models.Model):
    tamaño_actual = models.CharField(max_length=20)
    opciones = models.JSONField(default=list)

    def cambiar_tamaño(self, nuevo_tamaño):
        self.tamaño_actual = nuevo_tamaño
        self.save()

    def obtener_tamaño_actual(self):
        return self.tamaño_actual

    def __str__(self):
        return f"Tamaño: {self.tamaño_actual}"

class RecursosInclusion(models.Model):
    recursos = models.CharField(max_length=200)

    def buscar_recursos(self, query):
        # Lógica de búsqueda
        pass

    def descargar_recursos(self):
        # Lógica de descarga
        pass

    def __str__(self):
        return self.recursos