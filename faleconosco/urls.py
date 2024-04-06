from django.urls import path
from . import views

urlpatterns = [
    path('', views.faleconosco, name='faleconosco'),
]