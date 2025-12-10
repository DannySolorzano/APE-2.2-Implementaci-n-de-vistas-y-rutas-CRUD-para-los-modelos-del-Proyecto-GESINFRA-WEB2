from django.db import models

class Institucion(models.Model):
    codigo_ame = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    sostenimiento = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    carton = models.CharField(max_length=100)
    correo = models.EmailField()
    regimen_adaptivo = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return self.nombre


class Docente(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    comision = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class DocenteSalario(models.Model):
    codigo_docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='salarios')
    salario = models.IntegerField()  # D. Aigüeline

    class Meta:
        verbose_name = "Salario Docente"
        verbose_name_plural = "Salarios Docentes"

    def __str__(self):
        return f"Salario de {self.codigo_docente.nombre}"


class NivelDocente(models.Model):
    id = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=100)
    categoria = models.IntegerField()  # Casión

    class Meta:
        verbose_name = "Nivel Docente"
        verbose_name_plural = "Niveles Docentes"

    def __str__(self):
        return self.nivel


class Estudiante(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    correo_institucional = models.EmailField(blank=True, null=True)  # Correo adicional

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pensum(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Pensum"
        verbose_name_plural = "Pensums"

    def __str__(self):
        return self.nombre


class Calificacion(models.Model):
    codigo_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='calificaciones')
    asignatura = models.CharField(max_length=200)
    pensum = models.ForeignKey(Pensum, on_delete=models.CASCADE, related_name='calificaciones')
    nota1 = models.IntegerField()
    nota2 = models.IntegerField()
    nota3 = models.IntegerField()
    existencia_sumativa = models.IntegerField()
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='calificaciones_asignadas')
    fecha_registro = models.DateField()

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

    def __str__(self):
        return f"Calificación de {self.codigo_estudiante.nombre} en {self.asignatura}"

    def promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3