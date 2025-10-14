from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import (
    Trabajador, Asistencia, Accidente,
    Menu, Login, TipoTrabajador,
    SueldoTrabajador, EficienciaTrabajador,
    DesempenoTrabajador, FuncionesSistema
)
from .forms import (
    TrabajadorForm, AsistenciaForm, AccidenteForm
)

# Página de inicio
@login_required
def home(request):
    return render(request, 'core/home.html')

# Decorador común para las clases
login_decorators = [login_required]

# =======================
# CRUD: Trabajador
# =======================
@method_decorator(login_decorators, name='dispatch')
class TrabajadorList(ListView):
    model = Trabajador
    paginate_by = 10
    template_name = 'core/trabajador_list.html'


@method_decorator(login_decorators, name='dispatch')
class TrabajadorCreate(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'core/trabajador_form.html'
    success_url = reverse_lazy('core:trabajador_list')


@method_decorator(login_decorators, name='dispatch')
class TrabajadorUpdate(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'core/trabajador_form.html'
    success_url = reverse_lazy('core:trabajador_list')


@method_decorator(login_decorators, name='dispatch')
class TrabajadorDelete(DeleteView):
    model = Trabajador
    template_name = 'core/trabajador_confirm_delete.html'
    success_url = reverse_lazy('core:trabajador_list')


# =======================
# CRUD: Asistencia
# =======================
@method_decorator(login_decorators, name='dispatch')
class AsistenciaList(ListView):
    model = Asistencia
    paginate_by = 10
    template_name = 'core/asistencia_list.html'


@method_decorator(login_decorators, name='dispatch')
class AsistenciaCreate(CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'core/asistencia_form.html'
    success_url = reverse_lazy('core:asistencia_list')


@method_decorator(login_decorators, name='dispatch')
class AsistenciaUpdate(UpdateView):
    model = Asistencia
    form_class = AsistenciaForm
    template_name = 'core/asistencia_form.html'
    success_url = reverse_lazy('core:asistencia_list')


@method_decorator(login_decorators, name='dispatch')
class AsistenciaDelete(DeleteView):
    model = Asistencia
    template_name = 'core/asistencia_confirm_delete.html'
    success_url = reverse_lazy('core:asistencia_list')


# =======================
# CRUD: Accidente
# =======================
@method_decorator(login_decorators, name='dispatch')
class AccidenteList(ListView):
    model = Accidente
    paginate_by = 10
    template_name = 'core/accidente_list.html'


@method_decorator(login_decorators, name='dispatch')
class AccidenteCreate(CreateView):
    model = Accidente
    form_class = AccidenteForm
    template_name = 'core/accidente_form.html'
    success_url = reverse_lazy('core:accidente_list')


@method_decorator(login_decorators, name='dispatch')
class AccidenteUpdate(UpdateView):
    model = Accidente
    form_class = AccidenteForm
    template_name = 'core/accidente_form.html'
    success_url = reverse_lazy('core:accidente_list')


@method_decorator(login_decorators, name='dispatch')
class AccidenteDelete(DeleteView):
    model = Accidente
    template_name = 'core/accidente_confirm_delete.html'
    success_url = reverse_lazy('core:accidente_list')


# =======================
# CRUD: Tablas nuevas (sin relaciones)
# =======================
@method_decorator(login_decorators, name='dispatch')
class MenuList(ListView):
    model = Menu
    template_name = 'core/menu_list.html'


@method_decorator(login_decorators, name='dispatch')
class MenuCreate(CreateView):
    model = Menu
    fields = '__all__'
    template_name = 'core/menu_form.html'
    success_url = reverse_lazy('core:menu_list')


@method_decorator(login_decorators, name='dispatch')
class MenuUpdate(UpdateView):
    model = Menu
    fields = '__all__'
    template_name = 'core/menu_form.html'
    success_url = reverse_lazy('core:menu_list')


@method_decorator(login_decorators, name='dispatch')
class MenuDelete(DeleteView):
    model = Menu
    template_name = 'core/menu_confirm_delete.html'
    success_url = reverse_lazy('core:menu_list')


# Repetimos mismo patrón para cada tabla

@method_decorator(login_decorators, name='dispatch')
class LoginList(ListView):
    model = Login
    template_name = 'core/login_list.html'


@method_decorator(login_decorators, name='dispatch')
class LoginCreate(CreateView):
    model = Login
    fields = '__all__'
    template_name = 'core/login_form.html'
    success_url = reverse_lazy('core:login_list')


@method_decorator(login_decorators, name='dispatch')
class LoginUpdate(UpdateView):
    model = Login
    fields = '__all__'
    template_name = 'core/login_form.html'
    success_url = reverse_lazy('core:login_list')


@method_decorator(login_decorators, name='dispatch')
class LoginDelete(DeleteView):
    model = Login
    template_name = 'core/login_confirm_delete.html'
    success_url = reverse_lazy('core:login_list')


# Tipo Trabajador
@method_decorator(login_decorators, name='dispatch')
class TipoTrabajadorList(ListView):
    model = TipoTrabajador
    template_name = 'core/tipo_trabajador_list.html'


@method_decorator(login_decorators, name='dispatch')
class TipoTrabajadorCreate(CreateView):
    model = TipoTrabajador
    fields = '__all__'
    template_name = 'core/tipo_trabajador_form.html'
    success_url = reverse_lazy('core:tipo_trabajador_list')


@method_decorator(login_decorators, name='dispatch')
class TipoTrabajadorUpdate(UpdateView):
    model = TipoTrabajador
    fields = '__all__'
    template_name = 'core/tipo_trabajador_form.html'
    success_url = reverse_lazy('core:tipo_trabajador_list')


@method_decorator(login_decorators, name='dispatch')
class TipoTrabajadorDelete(DeleteView):
    model = TipoTrabajador
    template_name = 'core/tipo_trabajador_confirm_delete.html'
    success_url = reverse_lazy('core:tipo_trabajador_list')


# Sueldo, Eficiencia, Desempeño y FuncionesSistema
@method_decorator(login_decorators, name='dispatch')
class SueldoList(ListView):
    model = SueldoTrabajador
    template_name = 'core/sueldo_list.html'


@method_decorator(login_decorators, name='dispatch')
class SueldoCreate(CreateView):
    model = SueldoTrabajador
    fields = '__all__'
    template_name = 'core/sueldo_form.html'
    success_url = reverse_lazy('core:sueldo_list')


@method_decorator(login_decorators, name='dispatch')
class SueldoUpdate(UpdateView):
    model = SueldoTrabajador
    fields = '__all__'
    template_name = 'core/sueldo_form.html'
    success_url = reverse_lazy('core:sueldo_list')


@method_decorator(login_decorators, name='dispatch')
class SueldoDelete(DeleteView):
    model = SueldoTrabajador
    template_name = 'core/sueldo_confirm_delete.html'
    success_url = reverse_lazy('core:sueldo_list')


# Eficiencia
@method_decorator(login_decorators, name='dispatch')
class EficienciaList(ListView):
    model = EficienciaTrabajador
    template_name = 'core/eficiencia_list.html'


@method_decorator(login_decorators, name='dispatch')
class EficienciaCreate(CreateView):
    model = EficienciaTrabajador
    fields = '__all__'
    template_name = 'core/eficiencia_form.html'
    success_url = reverse_lazy('core:eficiencia_list')


@method_decorator(login_decorators, name='dispatch')
class EficienciaUpdate(UpdateView):
    model = EficienciaTrabajador
    fields = '__all__'
    template_name = 'core/eficiencia_form.html'
    success_url = reverse_lazy('core:eficiencia_list')


@method_decorator(login_decorators, name='dispatch')
class EficienciaDelete(DeleteView):
    model = EficienciaTrabajador
    template_name = 'core/eficiencia_confirm_delete.html'
    success_url = reverse_lazy('core:eficiencia_list')


# Desempeño
@method_decorator(login_decorators, name='dispatch')
class DesempenoList(ListView):
    model = DesempenoTrabajador
    template_name = 'core/desempeno_list.html'


@method_decorator(login_decorators, name='dispatch')
class DesempenoCreate(CreateView):
    model = DesempenoTrabajador
    fields = '__all__'
    template_name = 'core/desempeno_form.html'
    success_url = reverse_lazy('core:desempeno_list')


@method_decorator(login_decorators, name='dispatch')
class DesempenoUpdate(UpdateView):
    model = DesempenoTrabajador
    fields = '__all__'
    template_name = 'core/desempeno_form.html'
    success_url = reverse_lazy('core:desempeno_list')


@method_decorator(login_decorators, name='dispatch')
class DesempenoDelete(DeleteView):
    model = DesempenoTrabajador
    template_name = 'core/desempeno_confirm_delete.html'
    success_url = reverse_lazy('core:desempeno_list')


# FuncionesSistema
@method_decorator(login_decorators, name='dispatch')
class FuncionesList(ListView):
    model = FuncionesSistema
    template_name = 'core/funciones_list.html'


@method_decorator(login_decorators, name='dispatch')
class FuncionesCreate(CreateView):
    model = FuncionesSistema
    fields = '__all__'
    template_name = 'core/funciones_form.html'
    success_url = reverse_lazy('core:funciones_list')


@method_decorator(login_decorators, name='dispatch')
class FuncionesUpdate(UpdateView):
    model = FuncionesSistema
    fields = '__all__'
    template_name = 'core/funciones_form.html'
    success_url = reverse_lazy('core:funciones_list')


@method_decorator(login_decorators, name='dispatch')
class FuncionesDelete(DeleteView):
    model = FuncionesSistema
    template_name = 'core/funciones_confirm_delete.html'
    success_url = reverse_lazy('core:funciones_list')
