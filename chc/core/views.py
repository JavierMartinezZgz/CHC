from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        #Envío al template un diccionario de contexto que puedo visualizar
        return render(request, self.template_name, {'title': "Campus Homo Canis"})

class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filter'] = self.filterset
        return context

#def home(request):
#    return render(request, "core/home.html")

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

#def sample(request):
#    return render(request, "core/sample.html")

