from django.contrib import admin
from .models import Provincia

# Register your models here.
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    ordering = ('codigo',)
    
admin.site.register(Provincia, ProvinciaAdmin)