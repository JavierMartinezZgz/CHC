from django.contrib import admin
from .models import Servicio, TipoServicio

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tiposervicio', 'usuario', 'provincia',)

    class Media:
        css = {
            'all': ('servicios/css/custom_ckeditor.css',)
        }
admin.site.register(Servicio, ServicioAdmin)

class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre',)

admin.site.register(TipoServicio, TipoServicioAdmin)
