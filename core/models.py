from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Trabajador(models.Model):
    # Identificación
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    # Datos laborales
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
    estado = models.CharField(
        max_length=10,
        choices=[('ACTIVO', 'Activo'), ('INACTIVO', 'Inactivo')],
        default='ACTIVO'
    )

    # Contacto de emergencia
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

    # Sin relaciones: solo texto con RUTs separados por coma
    trabajadores_rut = models.CharField(
        max_length=500,
        blank=True,
        default='',
        help_text="RUTs involucrados separados por comas (ej: 11.111.111-1,22.222.222-2)"
    )

    def __str__(self):
        return f"{self.fecha} - {self.tipo} ({self.gravedad})"


class Asistencia(models.Model):
    # Sin relación ForeignKey
    trabajador_rut = models.CharField(
        max_length=12,
        blank=True,
        default='',
        help_text="RUT del trabajador"
    )
    trabajador_nombre = models.CharField(
        max_length=60,
        blank=True,
        default=''
    )
    trabajador_apellido = models.CharField(
        max_length=60,
        blank=True,
        default=''
    )

    fecha = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    minutos_atraso = models.PositiveIntegerField(default=0)
    horas_extras = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0)]
    )
    estado = models.CharField(max_length=12, choices=[
        ('PRESENTE', 'Presente'),
        ('AUSENTE', 'Ausente'),
        ('LICENCIA', 'Licencia'),
        ('VACACIONES', 'Vacaciones')
    ])
    observaciones = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('trabajador_rut', 'fecha')
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.trabajador_nombre} {self.trabajador_apellido} - {self.fecha} ({self.estado})"
    

class EficienciaTrabajador(models.Model):
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=60)
    id_eficiencia = models.IntegerField()
    trabajos_completados_en_1_mes = models.IntegerField(default=0)
    sueldo_promedio_informado = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.trabajador_nombre} - efic {self.id_eficiencia}"


class DesempenoTrabajador(models.Model):
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=60)
    id_desempeno = models.IntegerField()
    forma_de_hacer_trabajos = models.CharField(max_length=255, blank=True)
    posibles_quejas = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.trabajador_nombre} - desp {self.id_desempeno}"

class SueldoTrabajador(models.Model):
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=60)
    mes = models.CharField(max_length=20, help_text="Mes de cálculo")
    cantidad_trabajos_mes = models.PositiveIntegerField(default=0, help_text="Número de trabajos realizados en el mes")
    tipo_trabajos_mes = models.CharField(max_length=255, help_text="Descripción de los tipos de trabajos realizados")
    sueldo_total_mes = models.DecimalField(max_digits=12, decimal_places=2, default=0, help_text="Sueldo total correspondiente al mes")

    def __str__(self):
        return f"{self.trabajador_nombre} - {self.mes} (${self.sueldo_total_mes})"

