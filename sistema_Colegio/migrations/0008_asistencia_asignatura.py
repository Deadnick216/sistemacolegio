# Generated by Django 5.1.2 on 2024-12-14 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_Colegio', '0007_remove_docente_contrasena_docente_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='asignatura',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sistema_Colegio.asignatura'),
            preserve_default=False,
        ),
    ]
