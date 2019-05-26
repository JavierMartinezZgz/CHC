from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación') #Fecha de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición') #Fecha de modificacion

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']  #Ordenar descendente por el campo created
    
    def __str__(self):
        return self.title