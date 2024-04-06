from django.urls import path
from . import views

urlpatterns = [
    path('', views.cidades, name='cidades'),
    path('cadastar_cidade/', views.criar, name="cadastrar"),
    path('cadastarteste/', views.cadastrar, name="link_cadastrar")
]