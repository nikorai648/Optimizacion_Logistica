# core/migrations/0005_drop_legacy_fields_and_constraints.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_relations_and_datamigrate'),
    ]

    operations = [
        # 1) Asistencia unique_together pasa a usar el FK
        migrations.AlterUniqueTogether(
            name='asistencia',
            unique_together=set(),
        ),

        # 2) Hacer obligatorio el FK si ya no hay nulls (opcional; puedes dejar null=True si lo prefieres)
        migrations.AlterField(
            model_name='asistencia',
            name='trabajador',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.PROTECT, to='core.trabajador'),
        ),
        migrations.AlterUniqueTogether(
            name='asistencia',
            unique_together={('trabajador', 'fecha')},
        ),

        # 3) Eliminar campos legacy
        migrations.RemoveField(model_name='asistencia', name='trabajador_rut'),
        migrations.RemoveField(model_name='asistencia', name='trabajador_nombre'),
        migrations.RemoveField(model_name='asistencia', name='trabajador_apellido'),

        migrations.RemoveField(model_name='accidente', name='trabajadores_rut'),

        migrations.RemoveField(model_name='eficienciatrabajador', name='trabajador_rut'),
        migrations.RemoveField(model_name='eficienciatrabajador', name='trabajador_nombre'),

        migrations.RemoveField(model_name='desempenotrabajador', name='trabajador_rut'),
        migrations.RemoveField(model_name='desempenotrabajador', name='trabajador_nombre'),

        migrations.RemoveField(model_name='sueldotrabajador', name='trabajador_rut'),
        migrations.RemoveField(model_name='sueldotrabajador', name='trabajador_nombre'),
    ]
