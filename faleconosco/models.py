from django.db import models
from datetime import datetime


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=14)
    assunto = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    
