from django.contrib import admin
from .models import Evento, TipoEvento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipoevento', 'fechaEvento', 'usuario', 'provincia',)

    class Media:
        css = {
            'all': ('eventos/css/custom_ckeditor.css',)
        }
admin.site.register(Evento, EventoAdmin)

class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre',)

admin.site.register(TipoEvento, TipoEventoAdmin)
