import django_filters
from .models import Perro

class PerrosFilter(django_filters.FilterSet):
    class Meta:
        model = Perro
        fields = ['usuario', 'sexo', 'size', 'provincia']
