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
from .models import Evento
from .forms import EventoForm
from .filters import EventosFilter
from core.views import FilteredListView


class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            """return redirect(reverse_lazy('admin:login'))"""
            return redirect(reverse_lazy('login'))
        return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class EventoDetailView(DetailView):
    model = Evento

class EventoListView(FilteredListView):
    model = Evento
    filterset_class = EventosFilter
    template_name = 'eventos/evento_list.html'
    paginate_by = 8

def filtrarEventos(request):
    eventos_list = Evento.objects.all()
    eventos_filter = EventosFilter(request.GET, queryset=eventos_list)
    return render(request, 'eventos/evento_list.html', {'filter': eventos_filter})

class EventoCreate(LoginRequiredMixin, CreateView):
    model = Evento
    form_class = EventoForm
    success_url = reverse_lazy('eventos:eventos')
    
    def get_form(self, form_class=None):  #Para modificar el formulario en tiempo de ejecución
        form = super(EventoCreate, self).get_form()
        # Modificamos en tiempo real
        form.fields['usuario'].initial = self.request.user
        print(self.request.user)
        print(self.request.user.email)
        return form    

class EventoUpdate(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'eventos/evento_update_form.html'
    #template_name_suffix = '_update_form'

    def get_success_url(self):   #Mostramos de nuevo la página activa
        return reverse_lazy('eventos:update', args=[self.object.id]) + '?ok'

class EventoDelete(LoginRequiredMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos:eventos')