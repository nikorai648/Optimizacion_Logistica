# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    # =======================
    # Rutas CRUD: Trabajador
    # =======================
    path('trabajadores/', views.lista_trabajadores, name='trabajador_list'),
    path('trabajadores/nuevo/', views.crear_trabajador, name='trabajador_create'),
    path('trabajadores/<int:pk>/editar/', views.editar_trabajador, name='trabajador_update'),
    path('trabajadores/<int:pk>/eliminar/', views.eliminar_trabajador, name='trabajador_delete'),

    # =======================
    # Rutas CRUD: Asistencia
    # =======================
    path('asistencias/', views.lista_asistencias, name='asistencia_list'),
    path('asistencias/nueva/', views.crear_asistencia, name='asistencia_create'),
    path('asistencias/<int:pk>/editar/', views.editar_asistencia, name='asistencia_update'),
    path('asistencias/<int:pk>/eliminar/', views.eliminar_asistencia, name='asistencia_delete'),

    # =======================
    # Rutas CRUD: Accidente
    # =======================
    path('accidentes/', views.lista_accidentes, name='accidente_list'),
    path('accidentes/nuevo/', views.crear_accidente, name='accidente_create'),
    path('accidentes/<int:pk>/editar/', views.editar_accidente, name='accidente_update'),
    path('accidentes/<int:pk>/eliminar/', views.eliminar_accidente, name='accidente_delete'),

    # =======================
    # Rutas CRUD: Eficiencia
    # =======================
    path('eficiencia/', views.lista_eficiencia, name='eficiencia_list'),
    path('eficiencia/nueva/', views.crear_eficiencia, name='eficiencia_create'),
    path('eficiencia/<int:pk>/editar/', views.editar_eficiencia, name='eficiencia_update'),
    path('eficiencia/<int:pk>/eliminar/', views.eliminar_eficiencia, name='eficiencia_delete'),

    # =======================
    # Rutas CRUD: Desempeño
    # =======================
    path('desempeno/', views.lista_desempeno, name='desempeno_list'),
    path('desempeno/nuevo/', views.crear_desempeno, name='desempeno_create'),
    path('desempeno/<int:pk>/editar/', views.editar_desempeno, name='desempeno_update'),
    path('desempeno/<int:pk>/eliminar/', views.eliminar_desempeno, name='desempeno_delete'),

    # =======================
    # Rutas CRUD: Sueldos
    # =======================
    path('sueldos/', views.lista_sueldos, name='sueldo_list'),
    path('sueldos/nuevo/', views.crear_sueldo, name='sueldo_create'),
    path('sueldos/<int:pk>/editar/', views.editar_sueldo, name='sueldo_update'),
    path('sueldos/<int:pk>/eliminar/', views.eliminar_sueldo, name='sueldo_delete'),
]
