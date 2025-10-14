# core/urls.py
from django.urls import path
from . import views

app_name = 'core'  # permite usar nombres como core:trabajador_list

urlpatterns = [
    path('', views.home, name='home'),

    # Trabajador
    path('trabajadores/', views.TrabajadorList.as_view(), name='trabajador_list'),
    path('trabajadores/nuevo/', views.TrabajadorCreate.as_view(), name='trabajador_create'),
    path('trabajadores/<int:pk>/editar/', views.TrabajadorUpdate.as_view(), name='trabajador_update'),
    path('trabajadores/<int:pk>/eliminar/', views.TrabajadorDelete.as_view(), name='trabajador_delete'),

    # Asistencia
    path('asistencias/', views.AsistenciaList.as_view(), name='asistencia_list'),
    path('asistencias/nueva/', views.AsistenciaCreate.as_view(), name='asistencia_create'),
    path('asistencias/<int:pk>/editar/', views.AsistenciaUpdate.as_view(), name='asistencia_update'),
    path('asistencias/<int:pk>/eliminar/', views.AsistenciaDelete.as_view(), name='asistencia_delete'),

    # Accidente
    path('accidentes/', views.AccidenteList.as_view(), name='accidente_list'),
    path('accidentes/nuevo/', views.AccidenteCreate.as_view(), name='accidente_create'),
    path('accidentes/<int:pk>/editar/', views.AccidenteUpdate.as_view(), name='accidente_update'),
    path('accidentes/<int:pk>/eliminar/', views.AccidenteDelete.as_view(), name='accidente_delete'),

    # Menu
    path('menus/', views.MenuList.as_view(), name='menu_list'),
    path('menus/nuevo/', views.MenuCreate.as_view(), name='menu_create'),
    path('menus/<int:pk>/editar/', views.MenuUpdate.as_view(), name='menu_update'),
    path('menus/<int:pk>/eliminar/', views.MenuDelete.as_view(), name='menu_delete'),

    # Login
    path('logins/', views.LoginList.as_view(), name='login_list'),
    path('logins/nuevo/', views.LoginCreate.as_view(), name='login_create'),
    path('logins/<int:pk>/editar/', views.LoginUpdate.as_view(), name='login_update'),
    path('logins/<int:pk>/eliminar/', views.LoginDelete.as_view(), name='login_delete'),

    # TipoTrabajador
    path('tipos/', views.TipoTrabajadorList.as_view(), name='tipo_list'),
    path('tipos/nuevo/', views.TipoTrabajadorCreate.as_view(), name='tipo_create'),
    path('tipos/<int:pk>/editar/', views.TipoTrabajadorUpdate.as_view(), name='tipo_update'),
    path('tipos/<int:pk>/eliminar/', views.TipoTrabajadorDelete.as_view(), name='tipo_delete'),

    # SueldoTrabajador
    path('sueldos/', views.SueldoList.as_view(), name='sueldo_list'),
    path('sueldos/nuevo/', views.SueldoCreate.as_view(), name='sueldo_create'),
    path('sueldos/<int:pk>/editar/', views.SueldoUpdate.as_view(), name='sueldo_update'),
    path('sueldos/<int:pk>/eliminar/', views.SueldoDelete.as_view(), name='sueldo_delete'),

    # EficienciaTrabajador
    path('eficiencias/', views.EficienciaList.as_view(), name='eficiencia_list'),
    path('eficiencias/nuevo/', views.EficienciaCreate.as_view(), name='eficiencia_create'),
    path('eficiencias/<int:pk>/editar/', views.EficienciaUpdate.as_view(), name='eficiencia_update'),
    path('eficiencias/<int:pk>/eliminar/', views.EficienciaDelete.as_view(), name='eficiencia_delete'),

    # DesempenoTrabajador
    path('desempenos/', views.DesempenoList.as_view(), name='desempeno_list'),
    path('desempenos/nuevo/', views.DesempenoCreate.as_view(), name='desempeno_create'),
    path('desempenos/<int:pk>/editar/', views.DesempenoUpdate.as_view(), name='desempeno_update'),
    path('desempenos/<int:pk>/eliminar/', views.DesempenoDelete.as_view(), name='desempeno_delete'),

    # FuncionesSistema
    path('funciones/', views.FuncionesList.as_view(), name='funciones_list'),
    path('funciones/nuevo/', views.FuncionesCreate.as_view(), name='funciones_create'),
    path('funciones/<int:pk>/editar/', views.FuncionesUpdate.as_view(), name='funciones_update'),
    path('funciones/<int:pk>/eliminar/', views.FuncionesDelete.as_view(), name='funciones_delete'),
]
