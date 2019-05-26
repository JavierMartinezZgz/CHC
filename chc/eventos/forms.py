from django import forms
from .models import Evento
from django.contrib.auth.models import User

class EventoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        #print (kwargs)

    class Meta:
        model = Evento
        fields = ['usuario', 'nombre', 'tipoevento', 'fechaEvento', 'provincia', 'foto', 'link', 'descripcion']
        #Definimos los campos extendidos que usará el formulario
        widgets = {
            'usuario': forms.TextInput(attrs={'readonly': True}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}), 
            #'fechaEvento': forms.DateInput(attrs={'class':'form-control'}),
            'fechaEvento': forms.DateInput(attrs={'class':'form-control-date'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enlace mas informacion'}), 
            'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
        }
        labels = {
            'nombre': '', 'descripcion':'', 'link':''
        }