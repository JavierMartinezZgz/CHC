from django.urls import path
from .views import HomePageView, SamplePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sample/', SamplePageView.as_view(), name='sample'),
]

#Versión original

#from . import views

#urlpatterns = [
#    path('', views.home, name="home"),
#    path('sample/', views.sample, name="sample"),
#]