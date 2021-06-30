from django.contrib import admin
from .models import Personas, Donacion

# Register your models here.
class PersonasAdmin(admin.ModelAdmin):
    readonly_fields=['fecha']

admin.site.register(Personas, PersonasAdmin)
admin.site.register(Donacion)