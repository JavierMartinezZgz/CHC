from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#Función para borrar el anterior avatar y solo guardar el ultimo fichero
#def custom_upload_to(instance, filename):
#    old_instance = Profile.objects.get(pk=instance.pk) #Recuperamos el valor de la instancia anterior
#    old_instance.avatar.delete() #Borramos el archivo
#    return 'profiles/' + filename #Devolvemos el valor nuevo del archivo
#
# Se sustituye por django_cleanup
#
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    #avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

#Creamos una función (SEÑAL) que se asegure de crear un perfil cuando el usuario se registra
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False): #Solo se ejecuta cuando se crea la primera vez
        Profile.objects.get_or_create(user=instance)
        #print("Se acaba de crear un usuario y su perfil enlazado")