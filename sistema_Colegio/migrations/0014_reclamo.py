# Generated by Django 5.1.2 on 2024-12-16 23:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_Colegio', '0013_remove_nodocente_contrasena_nodocente_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_Colegio.estudiante')),
            ],
        ),
    ]
