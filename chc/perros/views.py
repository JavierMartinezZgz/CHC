from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
"""
Usando decoradores
"""
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
""""""
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Perro
from .forms import PerroForm
from .filters import PerrosFilter
from core.views import FilteredListView

class UserRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    Definimos el dispatch una vez y lo heredarán todas las clases hijas
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            """return redirect(reverse_lazy('admin:login'))"""
            return redirect(reverse_lazy('login'))
        return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)
    
"""
class StaffRequiredMixin(object):
    Usando decoradores que verifica que el usaurio es staff

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
"""

# Create your views here.

class PerroDetailView(DetailView):
    model = Perro

class PerroListView(FilteredListView):
    model = Perro
    filterset_class = PerrosFilter
    template_name = 'perros/perro_list.html'
    paginate_by = 8

#def filtrarPerros(request):
#    perros_list = Perro.objects.all()
#    perros_filter = PerrosFilter(request.GET, queryset=perros_list)
#    return render(request, 'perros/perro_list.html', {'filter': perros_filter})

class PerroCreate(LoginRequiredMixin, CreateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy('perros:perros')
    
    def get_form(self, form_class=None):  #Para modificar el formulario en tiempo de ejecución
        form = super(PerroCreate, self).get_form()
        form.fields['usuario'].initial = self.request.user
        return form    

class PerroUpdate(LoginRequiredMixin, UpdateView):
    model = Perro
    form_class = PerroForm
    template_name = 'perros/perro_update_form.html'
    #template_name_suffix = '_update_form'

    def get_success_url(self):   #Mostramos de nuevo la página activa
        return reverse_lazy('perros:update', args=[self.object.id]) + '?ok'

class PerroDelete(LoginRequiredMixin, DeleteView):
    model = Perro
    success_url = reverse_lazy('perros:perros')

def misperros(request, usuario):
    print(misperros)
    
    return reverse_lazy('perros:perros')

