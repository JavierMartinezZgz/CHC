from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.contrib.auth.models import User
from core.models import Provincia

CHOICE_SEXO = (('H','Hembra'),('M','Macho'))
CHOICE_SIZE = (
    ('Toy/Enano','< 5 kg'),
    ('Pequeño','5 - 14 kg'),
    ('Mediano','14 - 25 kg'),
    ('Grande','25 - 50 kg'),
    ('Gigante','> 50 kg')
)

class Perro(models.Model):
    nombre = models.CharField(max_length=30, verbose_name = 'Nombre')
    sexo = models.CharField(max_length=2, verbose_name = 'Sexo', choices=CHOICE_SEXO)
    usuario = models.ForeignKey(User, verbose_name = 'Responsable', on_delete=models.CASCADE)
    raza = models.CharField(max_length=30, verbose_name = 'Raza')
    nacimiento = models.IntegerField(verbose_name = 'Año de nacimiento', default=2000)
    size = models.CharField(max_length=10,verbose_name = 'Tamaño', choices=CHOICE_SIZE, default='Mediano')
    color = models.CharField(max_length=30, verbose_name = 'Color')
    foto = models.ImageField(verbose_name = 'Foto',upload_to="perros")
    descripcion = RichTextField(verbose_name = 'Descripción')
    link = models.URLField(null=True, blank=True, verbose_name = 'Mas información')
    provincia = models.ForeignKey(Provincia, verbose_name = 'Provincia', on_delete=models.CASCADE, default = '50')
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación') #Fecha de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edición') #Fecha de modificacion
    
    class Meta:
        verbose_name = 'perro'
        verbose_name_plural = 'perros'
        ordering = ["-updated"]  #Ordenar descendente por el campo created
    
    def __str__(self):
        return "{} ({}) - ({})".format(self.nombre, self.usuario, self.nacimiento)

