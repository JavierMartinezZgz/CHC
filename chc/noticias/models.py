from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.contrib.auth.models import User
from core.models import Provincia

class TipoNoticia(models.Model):
    tipo = models.CharField(max_length=2, verbose_name = 'Tipo Noticia')
    nombre = models.CharField(max_length=50, verbose_name = 'Nombre tipo Noticia')
    
    class Meta:
        verbose_name = 'tipo de noticia'
        verbose_name_plural = 'tipos de noticias'
        ordering = ["tipo"]  #Ordenar descendente por el campo created
    
    def __str__(self):
        return "{}".format(self.nombre)

class Noticia(models.Model):
    usuario = models.ForeignKey(User, verbose_name = 'Responsable', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, verbose_name = 'Nombre')
    tiponoticia = models.ForeignKey(TipoNoticia, verbose_name = 'Tipo', on_delete=models.CASCADE, default = '00')
    foto = models.ImageField(verbose_name = 'Foto', upload_to="noticias")
    fechaNoticia = models.DateField(verbose_name = 'Fecha de la noticia')
    descripcion = RichTextField(verbose_name = 'Descripción')
    link = models.URLField(null=True, blank=True, verbose_name = 'Mas información')
    provincia = models.ForeignKey(Provincia, verbose_name = 'Provincia', on_delete=models.CASCADE, default = '50')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación') #Fecha de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición') #Fecha de modificacion
    
    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'
        ordering = ["fechaNoticia"]  #Ordenar descendente por el campo created
    
    def __str__(self):
        return "{} ({})".format(self.nombre, self.fechaNoticia)

