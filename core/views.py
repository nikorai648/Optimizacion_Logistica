from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import (
    Trabajador, Asistencia, Accidente,
    EficienciaTrabajador, DesempenoTrabajador, SueldoTrabajador
)
from .forms import (
    TrabajadorForm, AsistenciaForm, AccidenteForm,
    EficienciaTrabajadorForm, DesempenoTrabajadorForm, SueldoTrabajadorForm
)

# =======================
# Página principal
# =======================
@login_required
def home(request):
    return render(request, 'core/home.html')


# =======================
# CRUD: Trabajador
# =======================
@login_required
def lista_trabajadores(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'core/trabajador_list.html', {'object_list': trabajadores})


@login_required
def crear_trabajador(request):
    form = TrabajadorForm()
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:trabajador_list')
    return render(request, 'core/trabajador_form.html', {'form': form})


@login_required
def editar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    form = TrabajadorForm(instance=trabajador)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('core:trabajador_list')
    return render(request, 'core/trabajador_form.html', {'form': form})


@login_required
def eliminar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('core:trabajador_list')
    return render(request, 'core/trabajador_confirm_delete.html', {'object': trabajador})


# =======================
# CRUD: Asistencia
# =======================
@login_required
def lista_asistencias(request):
    asistencias = Asistencia.objects.all()
    return render(request, 'core/asistencia_list.html', {'object_list': asistencias})


@login_required
def crear_asistencia(request):
    form = AsistenciaForm()
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:asistencia_list')
    return render(request, 'core/asistencia_form.html', {'form': form})


@login_required
def editar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    form = AsistenciaForm(instance=asistencia)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect('core:asistencia_list')
    return render(request, 'core/asistencia_form.html', {'form': form})


@login_required
def eliminar_asistencia(request, pk):
    asistencia = get_object_or_404(Asistencia, pk=pk)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('core:asistencia_list')
    return render(request, 'core/asistencia_confirm_delete.html', {'object': asistencia})


# =======================
# CRUD: Accidente
# =======================
@login_required
def lista_accidentes(request):
    accidentes = Accidente.objects.all()
    return render(request, 'core/accidente_list.html', {'object_list': accidentes})


@login_required
def crear_accidente(request):
    form = AccidenteForm()
    if request.method == 'POST':
        form = AccidenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:accidente_list')
    return render(request, 'core/accidente_form.html', {'form': form})


@login_required
def editar_accidente(request, pk):
    accidente = get_object_or_404(Accidente, pk=pk)
    form = AccidenteForm(instance=accidente)
    if request.method == 'POST':
        form = AccidenteForm(request.POST, instance=accidente)
        if form.is_valid():
            form.save()
            return redirect('core:accidente_list')
    return render(request, 'core/accidente_form.html', {'form': form})


@login_required
def eliminar_accidente(request, pk):
    accidente = get_object_or_404(Accidente, pk=pk)
    if request.method == 'POST':
        accidente.delete()
        return redirect('core:accidente_list')
    return render(request, 'core/accidente_confirm_delete.html', {'object': accidente})


# =======================
# CRUD: Eficiencia Trabajador
# =======================
@login_required
def lista_eficiencia(request):
    eficiencias = EficienciaTrabajador.objects.all()
    return render(request, 'core/eficiencia_list.html', {'object_list': eficiencias})


@login_required
def crear_eficiencia(request):
    form = EficienciaTrabajadorForm()
    if request.method == 'POST':
        form = EficienciaTrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:eficiencia_list')
    return render(request, 'core/eficiencia_form.html', {'form': form})


@login_required
def editar_eficiencia(request, pk):
    eficiencia = get_object_or_404(EficienciaTrabajador, pk=pk)
    form = EficienciaTrabajadorForm(instance=eficiencia)
    if request.method == 'POST':
        form = EficienciaTrabajadorForm(request.POST, instance=eficiencia)
        if form.is_valid():
            form.save()
            return redirect('core:eficiencia_list')
    return render(request, 'core/eficiencia_form.html', {'form': form})


@login_required
def eliminar_eficiencia(request, pk):
    eficiencia = get_object_or_404(EficienciaTrabajador, pk=pk)
    if request.method == 'POST':
        eficiencia.delete()
        return redirect('core:eficiencia_list')
    return render(request, 'core/eficiencia_confirm_delete.html', {'object': eficiencia})


# =======================
# CRUD: Desempeño Trabajador
# =======================
@login_required
def lista_desempeno(request):
    desempenos = DesempenoTrabajador.objects.all()
    return render(request, 'core/desempeno_list.html', {'object_list': desempenos})


@login_required
def crear_desempeno(request):
    form = DesempenoTrabajadorForm()
    if request.method == 'POST':
        form = DesempenoTrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:desempeno_list')
    return render(request, 'core/desempeno_form.html', {'form': form})


@login_required
def editar_desempeno(request, pk):
    desempeno = get_object_or_404(DesempenoTrabajador, pk=pk)
    form = DesempenoTrabajadorForm(instance=desempeno)
    if request.method == 'POST':
        form = DesempenoTrabajadorForm(request.POST, instance=desempeno)
        if form.is_valid():
            form.save()
            return redirect('core:desempeno_list')
    return render(request, 'core/desempeno_form.html', {'form': form})


@login_required
def eliminar_desempeno(request, pk):
    desempeno = get_object_or_404(DesempenoTrabajador, pk=pk)
    if request.method == 'POST':
        desempeno.delete()
        return redirect('core:desempeno_list')
    return render(request, 'core/desempeno_confirm_delete.html', {'object': desempeno})


# =======================
# CRUD: Sueldo Trabajador
# =======================
@login_required
def lista_sueldos(request):
    sueldos = SueldoTrabajador.objects.all()
    return render(request, 'core/sueldo_list.html', {'object_list': sueldos})


@login_required
def crear_sueldo(request):
    form = SueldoTrabajadorForm()
    if request.method == 'POST':
        form = SueldoTrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:sueldo_list')
    return render(request, 'core/sueldo_form.html', {'form': form})


@login_required
def editar_sueldo(request, pk):
    sueldo = get_object_or_404(SueldoTrabajador, pk=pk)
    form = SueldoTrabajadorForm(instance=sueldo)
    if request.method == 'POST':
        form = SueldoTrabajadorForm(request.POST, instance=sueldo)
        if form.is_valid():
            form.save()
            return redirect('core:sueldo_list')
    return render(request, 'core/sueldo_form.html', {'form': form})


@login_required
def eliminar_sueldo(request, pk):
    sueldo = get_object_or_404(SueldoTrabajador, pk=pk)
    if request.method == 'POST':
        sueldo.delete()
        return redirect('core:sueldo_list')
    return render(request, 'core/sueldo_confirm_delete.html', {'object': sueldo})
