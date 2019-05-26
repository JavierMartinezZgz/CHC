from django.urls import path
from .views import NoticiaListView, NoticiaDetailView, NoticiaCreate
from .views import NoticiaUpdate, NoticiaDelete

noticias_patterns = ([
    path('', NoticiaListView.as_view(), name='noticias'),
    #path('', filtrarEventos, name='eventos'),
    path('<int:pk>/<slug:slug>/', NoticiaDetailView.as_view(), name='noticia'),
    path('create/', NoticiaCreate.as_view(), name='create'),
    path('update/<int:pk>/', NoticiaUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', NoticiaDelete.as_view(), name='delete'),
], 'noticias')