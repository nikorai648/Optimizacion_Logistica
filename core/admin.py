from django.contrib import admin
from .models import Trabajador, Asistencia, Accidente

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ("rut", "nombre", "apellido", "cargo", "turno", "estado")
    search_fields = ("rut", "nombre", "apellido", "email", "cargo")
    list_filter = ("estado", "turno", "tipo_contrato", "area")


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("trabajador", "fecha", "estado", "minutos_atraso", "horas_extras")
    list_filter = ("estado", "fecha")
    search_fields = ("trabajador__nombre", "trabajador__apellido", "trabajador__rut")


@admin.register(Accidente)
class AccidenteAdmin(admin.ModelAdmin):
    list_display = ("fecha", "tipo", "gravedad", "lugar", "requiere_licencia", "dias_licencia", "involucrados")
    list_filter = ("gravedad", "requiere_licencia", "fecha")
    search_fields = ("tipo", "lugar", "reportado_a", "trabajadores__rut", "trabajadores__nombre", "trabajadores__apellido")
    filter_horizontal = ("trabajadores",)  # 👈 facilita seleccionar múltiples trabajadores

    def involucrados(self, obj):
        # Muestra cuántos trabajadores están asociados al accidente
        return obj.trabajadores.count()
    involucrados.short_description = "N° trabajadores"
