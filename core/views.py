from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import (
    Trabajador, Asistencia, Accidente,EficienciaTrabajador, DesempenoTrabajador
   
)
from .forms import (
    TrabajadorForm, AsistenciaForm, AccidenteForm, EficienciaTrabajadorForm, DesempenoTrabajadorForm
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


# ===== Eficiencia =====
@method_decorator(login_decorators, name='dispatch')
class EficienciaList(ListView):
    model = EficienciaTrabajador
    paginate_by = 10
    template_name = 'core/eficiencia_list.html'


@method_decorator(login_decorators, name='dispatch')
class EficienciaCreate(CreateView):
    model = EficienciaTrabajador
    form_class = EficienciaTrabajadorForm
    template_name = 'core/eficiencia_form.html'
    success_url = reverse_lazy('core:eficiencia_list')


@method_decorator(login_decorators, name='dispatch')
class EficienciaUpdate(UpdateView):
    model = EficienciaTrabajador
    form_class = EficienciaTrabajadorForm
    template_name = 'core/eficiencia_form.html'
    success_url = reverse_lazy('core:eficiencia_list')


@method_decorator(login_decorators, name='dispatch')
class EficienciaDelete(DeleteView):
    model = EficienciaTrabajador
    template_name = 'core/eficiencia_confirm_delete.html'
    success_url = reverse_lazy('core:eficiencia_list')


# ===== Desempeño =====
@method_decorator(login_decorators, name='dispatch')
class DesempenoList(ListView):
    model = DesempenoTrabajador
    paginate_by = 10
    template_name = 'core/desempeno_list.html'


@method_decorator(login_decorators, name='dispatch')
class DesempenoCreate(CreateView):
    model = DesempenoTrabajador
    form_class = DesempenoTrabajadorForm
    template_name = 'core/desempeno_form.html'
    success_url = reverse_lazy('core:desempeno_list')


@method_decorator(login_decorators, name='dispatch')
class DesempenoUpdate(UpdateView):
    model = DesempenoTrabajador
    form_class = DesempenoTrabajadorForm
    template_name = 'core/desempeno_form.html'
    success_url = reverse_lazy('core:desempeno_list')


@method_decorator(login_decorators, name='dispatch')
class DesempenoDelete(DeleteView):
    model = DesempenoTrabajador
    template_name = 'core/desempeno_confirm_delete.html'
    success_url = reverse_lazy('core:desempeno_list')


