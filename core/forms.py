from django import forms
from .models import DesempenoTrabajador, EficienciaTrabajador, FuncionesSistema, Trabajador, Asistencia, Accidente , Menu, Login, TipoTrabajador, SueldoTrabajador
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
class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"

class TipoTrabajadorForm(forms.ModelForm):
    class Meta:
        model = TipoTrabajador
        fields = "__all__"

class SueldoTrabajadorForm(forms.ModelForm):
    class Meta:
        model = SueldoTrabajador
        fields = "__all__"

class EficienciaTrabajadorForm(forms.ModelForm):
    class Meta:
        model = EficienciaTrabajador
        fields = "__all__"

class DesempenoTrabajadorForm(forms.ModelForm):
    class Meta:
        model = DesempenoTrabajador
        fields = "__all__"

class FuncionesSistemaForm(forms.ModelForm):
    class Meta:
        model = FuncionesSistema
        fields = "__all__"        
