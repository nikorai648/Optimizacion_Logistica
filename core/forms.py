from django import forms
from .models import Trabajador, Asistencia, Accidente, TrabajadorAccidente

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'

class AccidenteForm(forms.ModelForm):
    class Meta:
        model = Accidente
        fields = '__all__'