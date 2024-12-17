# Generated by Django 5.1.2 on 2024-12-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_Colegio', '0003_asignatura_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='asignaturas',
            field=models.ManyToManyField(related_name='docentes', to='sistema_Colegio.asignatura'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='asignaturas',
            field=models.ManyToManyField(related_name='estudiantes', to='sistema_Colegio.asignatura'),
        ),
    ]
