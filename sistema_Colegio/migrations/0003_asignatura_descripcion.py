# Generated by Django 5.1.2 on 2024-12-13 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_Colegio', '0002_nodocente_contrasena_nodocente_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
