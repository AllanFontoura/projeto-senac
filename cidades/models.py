from django.db import models
from datetime import datetime


class Cidade(models.Model):
    local = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now, blank=True)