# inventario/models.py
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoEquipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class EstadoEquipo(models.Model):
    estado = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.estado

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE)
    nombre_equipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    fecha_adquisicion = models.DateField()
    estado = models.ForeignKey(EstadoEquipo, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre_equipo} - {self.numero_serie}"