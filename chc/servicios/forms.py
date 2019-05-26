from django import forms
from .models import Servicio
from django.contrib.auth.models import User

class ServicioForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        #print (kwargs)

    class Meta:
        model = Servicio
        fields = ['usuario', 'nombre', 'tiposervicio', 'provincia', 'foto', 'link', 'descripcion']
        #Definimos los campos extendidos que usará el formulario
        widgets = {
            'usuario': forms.TextInput(attrs={'readonly': True}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}), 
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enlace mas informacion'}), 
            'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
        labels = {
            'nombre': '', 'descripcion':'', 'link':''
        }