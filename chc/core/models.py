from django.db import models

# Create your models here.

class Provincia(models.Model):
    codigo = models.CharField(max_length=2, verbose_name='Código', primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='Provincia')

    class Meta:
        verbose_name = 'provincia'
        verbose_name_plural = 'provincias'
        ordering = ['codigo']   
    
    def __str__(self):
        return self.nombre
    