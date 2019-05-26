from django.urls import path
from .views import ServicioListView, filtrarServicios, ServicioDetailView, ServicioCreate
from .views import ServicioUpdate, ServicioDelete

servicios_patterns = ([
    #path('', filtrarServicios, name='servicios'),
    path('', ServicioListView.as_view(), name='servicios'),
    path('<int:pk>/<slug:slug>/', ServicioDetailView.as_view(), name='servicio'),
    path('create/', ServicioCreate.as_view(), name='create'),
    path('update/<int:pk>/', ServicioUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ServicioDelete.as_view(), name='delete'),
], 'servicios')