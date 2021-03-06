# Generated by Django 3.2.4 on 2021-06-23 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre Completo')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('problema', models.TextField(verbose_name='Problema o Sugerencias')),
                ('vacunaciones', models.CharField(max_length=50, verbose_name='Vacunas')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Personas',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
