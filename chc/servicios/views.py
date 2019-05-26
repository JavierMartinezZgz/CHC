from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
"""
Usando decoradores
"""
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
""""""
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from .models import Servicio
from .forms import ServicioForm
from .filters import ServiciosFilter
from core.views import FilteredListView


class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            """return redirect(reverse_lazy('admin:login'))"""
            return redirect(reverse_lazy('login'))
        return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class ServicioDetailView(DetailView):
    model = Servicio

class ServicioListView(FilteredListView):
    model = Servicio
    filterset_class = ServiciosFilter
    template_name = 'servicios/servicio_list.html'
    paginate_by = 8

def filtrarServicios(request):
    servicios_list = Servicio.objects.all()
    servicios_filter = ServiciosFilter(request.GET, queryset=servicios_list)
    return render(request, 'servicios/servicio_list.html', {'filter': servicios_filter})

class ServicioCreate(LoginRequiredMixin, CreateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy('servicios:servicios')
    
    def get_form(self, form_class=None):  #Para modificar el formulario en tiempo de ejecución
        form = super(ServicioCreate, self).get_form()
        # Modificamos en tiempo real
        form.fields['usuario'].initial = self.request.user
        print(self.request.user)
        print(self.request.user.email)
        return form    

class ServicioUpdate(LoginRequiredMixin, UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicios/servicio_update_form.html'
    #template_name_suffix = '_update_form'

    def get_success_url(self):   #Mostramos de nuevo la página activa
        return reverse_lazy('servicios:update', args=[self.object.id]) + '?ok'

class ServicioDelete(LoginRequiredMixin, DeleteView):
    model = Servicio
    success_url = reverse_lazy('servicios:servicios')