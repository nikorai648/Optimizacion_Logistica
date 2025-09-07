from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Trabajador(models.Model):

    # Identificación Trabajador
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=60)
    area = models.CharField(max_length=60, blank=True)
    tipo_contrato = models.CharField(max_length=20, choices=[
        ('PLAZO_FIJO', 'Plazo fijo'),
        ('INDEFINIDO', 'Indefinido'),
        ('HONORARIOS', 'Honorarios'),
    ])
    turno = models.CharField(max_length=20, choices=[
        ('DIURNO', 'Diurno'), ('NOCTURNO', 'Nocturno'), ('ROTATIVO', 'Rotativo')
    ])
    fecha_ingreso = models.DateField()
    sueldo_base = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(max_length=10, choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')], default='ACTIVO')
    contacto_emergencia = models.CharField(max_length=100, blank=True)
    telefono_emergencia = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"
    

class Accidente(models.Model):
    fecha = models.DateField()
    tipo = models.CharField(max_length=60)
    gravedad = models.CharField(max_length=10, choices=[
        ('LEVE', 'Leve'), ('MODERADA', 'Moderada'), ('GRAVE', 'Grave'), ('FATAL', 'Fatal')
    ])
    lugar = models.CharField(max_length=120)
    hora_suceso = models.TimeField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    requiere_licencia = models.BooleanField(default=False)
    dias_licencia = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(365)])
    costo_estimado = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    reportado_a = models.CharField(max_length=120, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)

    trabajadores = models.ManyToManyField('Trabajador', related_name='accidentes', blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.tipo} ({self.gravedad})"


class Asistencia(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.RESTRICT, related_name='asistencias')
    fecha = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    minutos_atraso = models.PositiveIntegerField(default=0)
    horas_extras = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                       validators=[MinValueValidator(0)])
    estado = models.CharField(max_length=12, choices=[
        ('PRESENTE', 'Presente'), ('AUSENTE', 'Ausente'),
        ('LICENCIA', 'Licencia'), ('VACACIONES', 'Vacaciones')
    ])
    observaciones = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('trabajador', 'fecha')
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.trabajador} - {self.fecha} ({self.estado})"
    



