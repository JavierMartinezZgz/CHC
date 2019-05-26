from .models import Link

#Defino la función que permite aumentar el contexto. 
#Usar variables en todas las templates sin tener que inyectarlas
#El nombre de la función puede ser el que se quiera pero hay que meterlo en settings.py

def ctx_dict(request):
    ctx = {}  #Se crea un diccionario donde almacenar la clave y en el enlace
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx