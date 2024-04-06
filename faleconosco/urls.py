from django.urls import path
from . import views

urlpatterns = [
    path('', views.faleconosco, name='faleconosco'),
    path('contato/', views.enviar, name='enviar_contato'),
]