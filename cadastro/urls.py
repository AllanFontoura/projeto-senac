from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='cadastro'),
    path('cadastro/cliente', views.criar, name="criar_cliente"),
    path('deletar/cliente/<int:id_cliente>',views.deletar_cliente, name='deletar_cliente'),
    path('editar/cliente/<int:id_cliente>', views.editar, name='editar_cliente'),
    path('atualizar', views.atualizar_cliente, name="atualizar_cliente"),
    path('cadastro/lista_de_cliente', views.cadastro, name="listar_cliente"),
]