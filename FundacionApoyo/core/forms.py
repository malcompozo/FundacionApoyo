from django import forms
from .models import Personas,Donacion

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ['nombre', 'problema', 'vacunaciones', 'descripcion']
        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'problema': forms.Textarea(attrs={'class':'form-control'}),
            'vacunaciones': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }
        
class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['nombre', 'donacion', 'descripcion']
        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'donacion': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }