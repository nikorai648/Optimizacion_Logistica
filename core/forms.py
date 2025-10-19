from django import forms
from .models import  Trabajador, Asistencia, Accidente, EficienciaTrabajador, DesempenoTrabajador, SueldoTrabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = "__all__"

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"
        help_texts = {
            "trabajador_rut": "RUT del trabajador (sin relación a tabla).",
        }

class AccidenteForm(forms.ModelForm):
    class Meta:
        model = Accidente
        fields = "__all__"
        help_texts = {
            "trabajadores_rut": "Lista de RUTs separados por comas.",
        }

class EficienciaTrabajadorForm(forms.ModelForm):
    class Meta:
        model = EficienciaTrabajador
        fields = '__all__'


class DesempenoTrabajadorForm(forms.ModelForm):
    class Meta:
        model = DesempenoTrabajador
        fields = '__all__'


class SueldoTrabajadorForm(forms.ModelForm):
    class Meta:
        model = SueldoTrabajador
        fields = '__all__'