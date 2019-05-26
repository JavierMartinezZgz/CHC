from django.urls import path
from .views import EventoListView, filtrarEventos, EventoDetailView, EventoCreate
from .views import EventoUpdate, EventoDelete

eventos_patterns = ([
    path('', EventoListView.as_view(), name='eventos'),
    #path('', filtrarEventos, name='eventos'),
    path('<int:pk>/<slug:slug>/', EventoDetailView.as_view(), name='evento'),
    path('create/', EventoCreate.as_view(), name='create'),
    path('update/<int:pk>/', EventoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', EventoDelete.as_view(), name='delete'),
], 'eventos')