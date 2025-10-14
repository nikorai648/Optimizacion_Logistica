from django import forms
from .models import  Trabajador, Asistencia, Accidente 

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

