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

]