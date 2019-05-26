from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.contrib.auth.models import User
from core.models import Provincia

class TipoEvento(models.Model):
    tipo = models.CharField(max_length=2, verbose_name = 'Tipo Evento')
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre tipo Evento')
    
    class Meta:
        verbose_name = 'tipo de evento'
        verbose_name_plural = 'tipos de eventos'
        ordering = ["tipo"]  #Ordenar descendente por el campo created
    
    def __str__(self):
        return "{}".format(self.nombre)

class Evento(models.Model):
    usuario = models.ForeignKey(User, verbose_name = 'Responsable', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, verbose_name = 'Nombre')
    tipoevento = models.ForeignKey(TipoEvento, verbose_name = 'Tipo', on_delete=models.CASCADE, default = '00')
    foto = models.ImageField(verbose_name = 'Foto', upload_to="eventos")
    fechaEvento = models.DateField(verbose_name = 'Fecha del evento')
    descripcion = RichTextField(verbose_name = 'Descripción')
    link = models.URLField(null=True, blank=True, verbose_name = 'Mas información')
    provincia = models.ForeignKey(Provincia, verbose_name = 'Provincia', on_delete=models.CASCADE, default = '50')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación') #Fecha de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición') #Fecha de modificacion
    
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
        ordering = ["fechaEvento"]  #Ordenar descendente por el campo created
    
    def __str__(self):
        return "{} ({}) - ({})".format(self.nombre, self.usuario, self.fechaEvento)

