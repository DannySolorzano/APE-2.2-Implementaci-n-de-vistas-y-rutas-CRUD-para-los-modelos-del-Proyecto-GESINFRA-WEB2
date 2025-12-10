from django.db import models
from django.contrib.auth.models import User

class ConfiguracionAccesibilidad(models.Model):
    TAMANIO_FUENTE_CHOICES = [
        ('pequeno', 'Pequeño'),
        ('normal', 'Normal'),
        ('grande', 'Grande'),
        ('muy-grande', 'Muy Grande'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    alto_contraste = models.BooleanField(default=False)
    tamanio_fuente = models.CharField(max_length=20, choices=TAMANIO_FUENTE_CHOICES, default='normal')
    lectura_asistida = models.BooleanField(default=False)
    token_accesibilidad = models.CharField(max_length=100, default='normal')
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Configuración de {self.usuario.username if self.usuario else 'Sistema'}"
    
    def aplicar_estilos(self):
        return {
            'alto_contraste': self.alto_contraste,
            'tamanio_fuente': self.tamanio_fuente,
            'lectura_asistida': self.lectura_asistida,
        }


class TerminologiaEspecifica(models.Model):
    termino = models.CharField(max_length=200)
    definicion = models.TextField()
    categoria = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Terminología Específica"
        verbose_name_plural = "Terminologías Específicas"
    
    def __str__(self):
        return self.termino


class ControlTransicionesTexto(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.IntegerField(default=300, help_text="Duración en milisegundos")
    efecto = models.CharField(max_length=100, default='fade', 
                             choices=[('fade', 'Desvanecimiento'), ('slide', 'Deslizamiento'), 
                                      ('zoom', 'Zoom'), ('none', 'Sin efecto')])
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Control de Transiciones de Texto"
        verbose_name_plural = "Controles de Transiciones de Texto"
    
    def __str__(self):
        return self.nombre


class TokenInmunizacion(models.Model):
    TIPO_CHOICES = [
        ('acceso', 'Token de Acceso'),
        ('renovacion', 'Token de Renovación'),
        ('emergencia', 'Token de Emergencia'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    valor = models.CharField(max_length=500)
    fecha_expiracion = models.DateTimeField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Token de Inmunización"
        verbose_name_plural = "Tokens de Inmunización"
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
    
    def esta_expirado(self):
        from django.utils import timezone
        return timezone.now() > self.fecha_expiracion


class ContenidoAccesible(models.Model):
    TIPO_CHOICES = [
        ('texto', 'Texto'),
        ('imagen', 'Imagen'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    contenido = models.TextField()
    descripcion_alt = models.TextField(blank=True, help_text="Descripción alternativa para accesibilidad")
    transcript = models.TextField(blank=True, help_text="Transcript para contenido de audio/video")
    replicado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_replicacion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "Contenido Accesible"
        verbose_name_plural = "Contenidos Accesibles"
    
    def __str__(self):
        return self.titulo


class RecursoAccesible(models.Model):
    TIPO_RECURSO_CHOICES = [
        ('documento', 'Documento'),
        ('herramienta', 'Herramienta'),
        ('plugin', 'Plugin'),
        ('api', 'API'),
        ('servicio', 'Servicio'),
    ]
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_RECURSO_CHOICES)
    descripcion = models.TextField()
    url = models.URLField(blank=True)
    linkedin_reunachio = models.CharField(max_length=300, blank=True, 
                                         help_text="Integración con LinkedIn Reunachio")
    descriptor = models.CharField(max_length=500, help_text="Descriptores del recurso")
    activo = models.BooleanField(default=True)
    almacenamiento_recurrente = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Recurso Accesible"
        verbose_name_plural = "Recursos Accesibles"
    
    def __str__(self):
        return self.nombre


class FiltroRecurso(models.Model):
    recurso = models.ForeignKey(RecursoAccesible, on_delete=models.CASCADE, related_name='filtros')
    tipo_filtro = models.CharField(max_length=100)
    valor = models.CharField(max_length=500)
    prioridad = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = "Filtro de Recurso"
        verbose_name_plural = "Filtros de Recursos"
    
    def __str__(self):
        return f"{self.tipo_filtro}: {self.valor}"


class LogAccesibilidad(models.Model):
    TIPO_ACCION_CHOICES = [
        ('configuracion', 'Cambio de Configuración'),
        ('lectura', 'Lectura Asistida'),
        ('token', 'Uso de Token'),
        ('replicacion', 'Replicación de Contenido'),
        ('filtro', 'Filtrado de Recursos'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_accion = models.CharField(max_length=20, choices=TIPO_ACCION_CHOICES)
    descripcion = models.TextField()
    datos = models.JSONField(default=dict, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Log de Accesibilidad"
        verbose_name_plural = "Logs de Accesibilidad"
    
    def __str__(self):
        return f"{self.tipo_accion} - {self.fecha}"