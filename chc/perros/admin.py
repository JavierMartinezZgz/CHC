from django.contrib import admin
from .models import Perro

# Register your models here.
class PerroAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre', 'nacimiento', 'sexo', 'size', 'usuario', 'provincia')
    ordering = ('nacimiento',)
    #list_filter = ('usuario__username', 'sexo', 'size')
    list_filter = ('usuario__username', 'sexo', 'size')
    #search_fields = ['nacimiento']
    list_per_page = 20

    def post_campo(self, obj): #Ver clase 42
        return "ALGO"
    post_campo.short_description = "PLUS"

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
admin.site.register(Perro, PerroAdmin)
