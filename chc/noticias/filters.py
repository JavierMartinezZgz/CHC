import django_filters
from .models import Noticia

class NoticiasFilter(django_filters.FilterSet):
    class Meta:
        model = Noticia
        fields = ['usuario', 'tiponoticia', 'provincia']
