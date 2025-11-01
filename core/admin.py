from django.contrib import admin
from .models import (
    TipoTrabajador, Trabajador, Asistencia, Accidente,
    EficienciaTrabajador, DesempenoTrabajador, SueldoTrabajador
)

@admin.register(TipoTrabajador)
class TipoTrabajadorAdmin(admin.ModelAdmin):
    list_display  = ("rol_cargo", "tipo_contrato")
    search_fields = ("rol_cargo", "tipo_contrato")


@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display  = ("rut", "nombre", "apellido", "tipo", "turno", "estado")
    list_filter   = ("estado", "turno", "tipo__tipo_contrato", "tipo__rol_cargo")
    search_fields = ("rut", "nombre", "apellido", "email", "area")


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display  = ("trabajador", "fecha", "estado", "minutos_atraso", "horas_extras")
    list_filter   = ("estado", "fecha", "trabajador")
    search_fields = ("trabajador__rut", "trabajador__nombre", "trabajador__apellido")


@admin.register(Accidente)
class AccidenteAdmin(admin.ModelAdmin):
    list_display  = ("fecha", "tipo", "gravedad", "lugar", "requiere_licencia",
                     "dias_licencia", "mostrar_trabajadores")
    list_filter   = ("gravedad", "requiere_licencia", "fecha")
    search_fields = ("tipo", "lugar", "reportado_a",
                     "trabajadores__rut", "trabajadores__nombre", "trabajadores__apellido")

    def mostrar_trabajadores(self, obj):
        # Muestra hasta 5 RUTs, luego “(+N)”
        ruts = [t.rut for t in obj.trabajadores.all()[:5]]
        extra = obj.trabajadores.count() - len(ruts)
        return ", ".join(ruts) + (f" (+{extra})" if extra > 0 else "")
    mostrar_trabajadores.short_description = "Trabajadores (RUTs)"


@admin.register(EficienciaTrabajador)
class EficienciaAdmin(admin.ModelAdmin):
    list_display  = ("trabajador", "id_eficiencia",
                     "trabajos_completados_en_1_mes", "sueldo_promedio_informado")
    search_fields = ("trabajador__rut", "trabajador__nombre", "trabajador__apellido")


@admin.register(DesempenoTrabajador)
class DesempenoAdmin(admin.ModelAdmin):
    list_display  = ("trabajador", "id_desempeno",
                     "forma_de_hacer_trabajos", "posibles_quejas")
    search_fields = ("trabajador__rut", "trabajador__nombre", "trabajador__apellido")


@admin.register(SueldoTrabajador)
class SueldoTrabajadorAdmin(admin.ModelAdmin):
    list_display  = ("trabajador", "mes", "cantidad_trabajos_mes",
                     "sueldo_total_mes", "eficiencia")
    list_filter   = ("mes", "trabajador")
    search_fields = ("trabajador__rut", "trabajador__nombre", "trabajador__apellido", "mes")
