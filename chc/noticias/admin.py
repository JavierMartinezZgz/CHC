from django.contrib import admin
from .models import Noticia, TipoNoticia
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class NoticiaResource(resources.ModelResource):

    class Meta:
        model = Noticia
        
# class NoticiaAdmin(admin.ModelAdmin):
class NoticiaAdmin(ImportExportModelAdmin):
    list_display = ('nombre', 'tiponoticia', 'fechaNoticia', 'usuario', 'provincia',)
    resource_class = NoticiaResource

    class Media:
        css = {
            'all': ('noticias/css/custom_ckeditor.css',)
        }
admin.site.register(Noticia, NoticiaAdmin)

class TipoNoticiaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre',)

admin.site.register(TipoNoticia, TipoNoticiaAdmin)

