# Generated by Django 5.1.2 on 2024-12-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_Colegio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodocente',
            name='contrasena',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nodocente',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nodocente',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
