# core/migrations/0004_relations_and_datamigrate.py
from django.db import migrations, models
import django.db.models.deletion

def forwards_link_data(apps, schema_editor):
    Trabajador = apps.get_model('core', 'Trabajador')
    Asistencia = apps.get_model('core', 'Asistencia')
    Accidente = apps.get_model('core', 'Accidente')
    EficienciaTrabajador = apps.get_model('core', 'EficienciaTrabajador')
    DesempenoTrabajador = apps.get_model('core', 'DesempenoTrabajador')
    SueldoTrabajador = apps.get_model('core', 'SueldoTrabajador')

    rut_index = {t.rut: t.id for t in Trabajador.objects.all()}

    # Asistencia
    for a in Asistencia.objects.all():
        t_id = rut_index.get(a.trabajador_rut)
        if t_id:
            Asistencia.objects.filter(pk=a.pk).update(trabajador_id=t_id)

    # Eficiencia
    for e in EficienciaTrabajador.objects.all():
        t_id = rut_index.get(e.trabajador_rut)
        if t_id:
            EficienciaTrabajador.objects.filter(pk=e.pk).update(trabajador_id=t_id)

    # Desempeño
    for d in DesempenoTrabajador.objects.all():
        t_id = rut_index.get(d.trabajador_rut)
        if t_id:
            DesempenoTrabajador.objects.filter(pk=d.pk).update(trabajador_id=t_id)

    # Sueldos
    for s in SueldoTrabajador.objects.all():
        t_id = rut_index.get(s.trabajador_rut)
        if t_id:
            SueldoTrabajador.objects.filter(pk=s.pk).update(trabajador_id=t_id)

    # Accidente (migrar texto a M2M)
    for acc in Accidente.objects.all():
        if not acc.trabajadores_rut:
            continue
        ruts = [r.strip() for r in acc.trabajadores_rut.split(',') if r.strip()]
        ids = [rut_index[r] for r in ruts if r in rut_index]
        if ids:
            acc.trabajadores.set(ids)

def reverse_noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_sueldotrabajador_mes'),
    ]

    operations = [
        # 🔹 FK en Trabajador hacia TipoTrabajador (ya existe el modelo)
        migrations.AddField(
            model_name='trabajador',
            name='tipo',
            field=models.ForeignKey(
                null=True, blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='core.tipotrabajador'
            ),
        ),

        # 🔹 FKs a Trabajador
        migrations.AddField(
            model_name='asistencia',
            name='trabajador',
            field=models.ForeignKey(
                null=True, blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='core.trabajador'
            ),
        ),
        migrations.AddField(
            model_name='eficienciatrabajador',
            name='trabajador',
            field=models.ForeignKey(
                null=True, blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='core.trabajador'
            ),
        ),
        migrations.AddField(
            model_name='desempenotrabajador',
            name='trabajador',
            field=models.ForeignKey(
                null=True, blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='core.trabajador'
            ),
        ),
        migrations.AddField(
            model_name='sueldotrabajador',
            name='trabajador',
            field=models.ForeignKey(
                null=True, blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='core.trabajador'
            ),
        ),

        # 🔹 Relación opcional Sueldo–Eficiencia
        migrations.AddField(
            model_name='sueldotrabajador',
            name='eficiencia',
            field=models.ForeignKey(
                null=True, blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='core.eficienciatrabajador'
            ),
        ),

        # 🔹 ManyToMany de Accidentes a Trabajadores
        migrations.AddField(
            model_name='accidente',
            name='trabajadores',
            field=models.ManyToManyField(blank=True, to='core.trabajador'),
        ),

        # 🔹 Migrar datos existentes
        migrations.RunPython(forwards_link_data, reverse_noop),
    ]
