# Generated by Django 3.2.4 on 2021-06-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('donacion', models.IntegerField(verbose_name='Donación')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Donación',
                'verbose_name_plural': 'Donaciones',
            },
        ),
        migrations.AlterModelOptions(
            name='personas',
            options={'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
    ]