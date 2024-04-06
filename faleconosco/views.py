from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Contato

def faleconosco(request):
    return render(request, 'faleconosco.html')

def enviar(request):
    nome = request.POST['nome']
    email = request.POST['email']
    telefone = request.POST['telefone']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']
    contato = Contato.objects.create(nome=nome, email=email, telefone=telefone, assunto=assunto, mensagem=mensagem)
    contato.save()
    return redirect('faleconosco')