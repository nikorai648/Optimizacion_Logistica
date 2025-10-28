from django.contrib import admin
from .models import Trabajador, Asistencia, Accidente, EficienciaTrabajador, DesempenoTrabajador, SueldoTrabajador


class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ["rut", "nombre", "apellido", "cargo", "turno", "estado"]
    search_fields = ["rut", "nombre", "apellido", "email", "cargo"]
    list_filter = ["estado", "turno", "tipo_contrato", "area"]


class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ["trabajador_rut", "trabajador_nombre", "trabajador_apellido", "fecha", "estado", "minutos_atraso", "horas_extras"]
    list_filter = ["estado", "fecha"]
    search_fields = ["trabajador_rut", "trabajador_nombre", "trabajador_apellido"]


class AccidenteAdmin(admin.ModelAdmin):
    list_display = ["fecha", "tipo", "gravedad", "lugar", "requiere_licencia", "dias_licencia", "mostrar_trabajadores"]
    list_filter = ["gravedad", "requiere_licencia", "fecha"]
    search_fields = ["tipo", "lugar", "reportado_a", "trabajadores_rut"]

    def mostrar_trabajadores(self, obj):
        return obj.trabajadores_rut
    mostrar_trabajadores.short_description = "Trabajadores (RUTs)"


class EficienciaAdmin(admin.ModelAdmin):
    list_display = ["trabajador_rut", "trabajador_nombre", "id_eficiencia", "trabajos_completados_en_1_mes", "sueldo_promedio_informado"]
    search_fields = ["trabajador_rut", "trabajador_nombre"]


class DesempenoAdmin(admin.ModelAdmin):
    list_display = ["trabajador_rut", "trabajador_nombre", "id_desempeno", "forma_de_hacer_trabajos", "posibles_quejas"]
    search_fields = ["trabajador_rut", "trabajador_nombre"]


class SueldoTrabajadorAdmin(admin.ModelAdmin):
    list_display = ["trabajador_rut", "trabajador_nombre", "mes", "cantidad_trabajos_mes", "sueldo_total_mes"]
    search_fields = ["trabajador_rut", "trabajador_nombre", "mes"]


# Registro de todos los modelos
admin.site.register(Trabajador, TrabajadorAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Accidente, AccidenteAdmin)
admin.site.register(EficienciaTrabajador, EficienciaAdmin)
admin.site.register(DesempenoTrabajador, DesempenoAdmin)
admin.site.register(SueldoTrabajador, SueldoTrabajadorAdmin)




