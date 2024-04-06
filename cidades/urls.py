from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='cidades'),
    path('cadastar_cidade', views.criar, name="cadastrar"),
    path('cadastar/cidade', views.cadastrar, name="link_cadastrar"),
    path('deletar/cidade/<int:id_cidade>',views.deletar_cidade, name='deletar_cidade'),
    path('editar/cidade/<int:id_cidade>', views.editar, name='editar_cidade'),
    path('atualizar', views.atualizar_cidade, name="atualizar_cidade"),

]