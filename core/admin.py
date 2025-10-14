from django.contrib import admin
from .models import DesempenoTrabajador, EficienciaTrabajador, FuncionesSistema, Trabajador, Asistencia, Accidente , Menu, Login, TipoTrabajador, SueldoTrabajador
   

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ("rut", "nombre", "apellido", "cargo", "turno", "estado")
    search_fields = ("rut", "nombre", "apellido", "email", "cargo")
    list_filter = ("estado", "turno", "tipo_contrato", "area")


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("trabajador_rut", "trabajador_nombre", "trabajador_apellido", "fecha", "estado", "minutos_atraso", "horas_extras")
    list_filter = ("estado", "fecha")
    search_fields = ("trabajador_rut", "trabajador_nombre", "trabajador_apellido")


@admin.register(Accidente)
class AccidenteAdmin(admin.ModelAdmin):
    list_display = ("fecha", "tipo", "gravedad", "lugar", "requiere_licencia", "dias_licencia", "mostrar_trabajadores")
    list_filter = ("gravedad", "requiere_licencia", "fecha")
    search_fields = ("tipo", "lugar", "reportado_a", "trabajadores_rut")

    def mostrar_trabajadores(self, obj):
        return obj.trabajadores_rut
    mostrar_trabajadores.short_description = "Trabajadores (RUTs)"

admin.site.register(Menu)
admin.site.register(Login)
admin.site.register(TipoTrabajador)
admin.site.register(SueldoTrabajador)
admin.site.register(EficienciaTrabajador)
admin.site.register(DesempenoTrabajador)
admin.site.register(FuncionesSistema)

