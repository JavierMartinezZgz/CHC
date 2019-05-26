import django_filters
from .models import Evento

class EventosFilter(django_filters.FilterSet):
    class Meta:
        model = Evento
        fields = ['usuario', 'tipoevento', 'provincia']
