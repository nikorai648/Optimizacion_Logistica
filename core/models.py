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
    

# ===== Tablas adicionales para segunda prueba (sin relaciones) =====

class Menu(models.Model):
    tipo_usuario = models.IntegerField()
    menu_col = models.CharField(max_length=45)
    login_nombre_usuario = models.CharField(max_length=60)  # referencia blanda (texto)

    def __str__(self):
        return f"{self.menu_col} (tipo {self.tipo_usuario})"


class Login(models.Model):
    nombre_usuario = models.CharField(max_length=60, unique=True)
    contrasena_usuario = models.CharField(max_length=128)  # (puedes guardar hash)
    funciones_sistema_busqueda_por_id = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.nombre_usuario


class TipoTrabajador(models.Model):
    rol_o_cargo = models.CharField(max_length=80)
    tipo_contrato = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.rol_o_cargo} - {self.tipo_contrato}"


class SueldoTrabajador(models.Model):
    # SIN FK: guardamos identificación textual del trabajador
    trabajador_rut = models.CharField(max_length=12)
    trabajador_nombre = models.CharField(max_length=60)

    sueldo_promedio = models.IntegerField()
    sueldo_por_trabajos_hechos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.trabajador_nombre} - ${self.sueldo_promedio}"


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


class FuncionesSistema(models.Model):
    busqueda_por_id = models.IntegerField()
    eliminar_datos_trabajador = models.CharField(max_length=60, blank=True)
    agregar_datos_trabajador = models.CharField(max_length=60, blank=True)
    actualizar_datos_trabajador = models.CharField(max_length=60, blank=True)
    trabajador_nombre = models.CharField(max_length=60)

    def __str__(self):
        return f"Funciones de {self.trabajador_nombre}"

