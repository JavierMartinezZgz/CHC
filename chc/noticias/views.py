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
from .models import Noticia
from .forms import NoticiaForm
from .filters import NoticiasFilter
from core.views import FilteredListView


class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            """return redirect(reverse_lazy('admin:login'))"""
            return redirect(reverse_lazy('login'))
        return super(UserRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class NoticiaDetailView(DetailView):
    model = Noticia

class NoticiaListView(FilteredListView):
    model = Noticia
    filterset_class = NoticiasFilter
    template_name = 'noticias/noticia_list.html'
    paginate_by = 8

class NoticiaCreate(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticias:noticias')
    
    def get_form(self, form_class=None):  #Para modificar el formulario en tiempo de ejecución
        form = super(NoticiaCreate, self).get_form()
        # Modificamos en tiempo real
        form.fields['usuario'].initial = self.request.user
        print(self.request.user)
        print(self.request.user.email)
        return form    

class NoticiaUpdate(LoginRequiredMixin, UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticia_update_form.html'
    #template_name_suffix = '_update_form'

    def get_success_url(self):   #Mostramos de nuevo la página activa
        return reverse_lazy('noticias:update', args=[self.object.id]) + '?ok'

class NoticiaDelete(LoginRequiredMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:noticias')