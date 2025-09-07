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