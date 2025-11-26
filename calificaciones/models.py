# calificaciones/models.py
from django.db import models

class Institucion(models.Model):
    codigo_amie = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    sostenimiento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    canton = models.CharField(max_length=50)
    correo = models.EmailField()
    regimen_educativo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    contacto = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class NivelEducativo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nivel = models.CharField(max_length=50)
    grado = models.IntegerField()

    def __str__(self):
        return f"{self.nivel} - {self.grado}"

class Estudiante(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    genero = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Paralelo(models.Model):
    grado = models.IntegerField()
    año_lectivo = models.CharField(max_length=9)
    nombre = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.grado}{self.nombre} - {self.año_lectivo}"

class Directivo(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    cargo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.cargo}: {self.nombre} {self.apellido}"

class Calificacion(models.Model):
    cedula_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.CharField(max_length=100)
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE)
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    nota3 = models.IntegerField()
    evaluacion_sumativa = models.IntegerField()
    periodo = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Calificación {self.asignatura} - {self.cedula_estudiante}"

# Create your models here.
