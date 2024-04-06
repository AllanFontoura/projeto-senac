from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Cidade

def cidades(request):
    return render(request, 'cidades.html')

def criar(request):
    local = request.POST['local']
    telefone = request.POST['telefone']
    email = request.POST['email']
    cidad = Cidade.objects.create(local=local, telefone=telefone, email=email)
    cidad.save()
    return redirect('cidades')

def cidade(request):
    lista_cidade = Cidade.objects.all()
    return render(request, 'cidades.html', {'lista_cidade': lista_cidade})

def cadastrar(request):
    return render(request, 'cadastrar_cidade.html')