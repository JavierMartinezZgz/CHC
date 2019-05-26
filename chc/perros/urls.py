from django.urls import path
from .views import PerroListView, PerroDetailView
from .views import PerroCreate, PerroUpdate, PerroDelete

perros_patterns = ([
    path('', PerroListView.as_view(), name='perros'),
    #path('', filtrarPerros, name='perros'),
    path('<int:pk>/<slug:slug>/', PerroDetailView.as_view(), name='perro'),
    path('create/', PerroCreate.as_view(), name='create'),
    path('update/<int:pk>/', PerroUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PerroDelete.as_view(), name='delete'),
], 'perros')