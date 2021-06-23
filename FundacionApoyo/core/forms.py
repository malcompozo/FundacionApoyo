from django.forms import ModelForm
from .models import Personas

class PersonaForm(ModelForm):
    class Meta:
        model = Personas
        fields = ['nombre', 'fecha', 'problema', 'vacunaciones', 'descripcion']