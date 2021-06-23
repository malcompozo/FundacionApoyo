from django import forms
from .models import Personas

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['nombre', 'fecha', 'problema', 'vacunaciones', 'descripcion']
        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}),
            'problema': forms.Textarea(attrs={'class':'form-control'}),
            'vacunaciones': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }