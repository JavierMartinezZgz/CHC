from django import forms
from .models import Perro
from django.contrib.auth.models import User

class PerroForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PerroForm, self).__init__(*args, **kwargs)
        #print (kwargs)

    class Meta:
        model = Perro

        fields = ['usuario', 'nombre', 'nacimiento', 'provincia', 'sexo', 'color', 'raza', 'size', 'foto', 'link', 'descripcion']
        #Definimos los campos extendidos que usará el formulario
        widgets = {
            'usuario': forms.TextInput(attrs={'readonly': True}),
            'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'color': forms.TextInput(attrs={'placeholder':'Color'}), 
            'raza': forms.TextInput(attrs={'placeholder':'Raza'}), 
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enlace mas informacion'}), 
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre': '', 'descripcion':'Descripción:', 'link':''
        }