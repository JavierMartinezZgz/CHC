from django.urls import path
from . import views

pages_patterns = [
    #Path de las url
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
    
]