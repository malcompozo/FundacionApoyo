from django.db import models
from django.db.models import Sum
from django.utils.timezone import now


class Personas(models.Model):
    nombre = models.CharField(max_length=40,verbose_name='Nombre Completo')
    fecha = models.DateTimeField(default=now,verbose_name='Fecha')
    problema = models.TextField(verbose_name='Problema o Sugerencias')
    vacunaciones = models.CharField(max_length=50, verbose_name='Vacunas')
    descripcion = models.TextField(verbose_name='Descripción')
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return self.nombre
    
class Donacion(models.Model):
    nombre = models.CharField(max_length=40,verbose_name='Nombre')
    donacion = models.IntegerField(verbose_name='Donación')
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Donación'
        verbose_name_plural = 'Donaciones'
    
    def __str__(self):
        return self.nombre
    
class Suma(models.Model):
    suma = Donacion.objects.aggregate(total_donaciones=Sum('donacion'))
    
    class Meta:
        verbose_name = 'Total de donaciones'
        verbose_name_plural = 'Total de donaciones'
    
    def __str__(self):
        return self.nombre