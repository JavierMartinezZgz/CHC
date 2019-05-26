import django_filters
from .models import Servicio

class ServiciosFilter(django_filters.FilterSet):
    class Meta:
        model = Servicio
        fields = ['usuario', 'tiposervicio', 'provincia']
