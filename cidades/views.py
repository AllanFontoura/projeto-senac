from django.shortcuts import render, redirect, get_object_or_404
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

def listar(request):
    lista_cidade = Cidade.objects.all()
    return render(request, 'cidades.html', {'lista': lista_cidade})

def cadastrar(request):
    return render(request, 'cadastrar_cidade.html')

def deletar_cidade(request, id_cidade):
    cidade= get_object_or_404(Cidade, pk=id_cidade)
    cidade.delete()
    return redirect('cidades')

def editar(request, id_cidade):
    cidade = get_object_or_404(Cidade, pk=id_cidade)
    return render(request, 'editar_cidade.html', {'dados_cidade': cidade})

def atualizar_cidade(request):
    id_cidade = request.POST["id"]
    cidade = Cidade.objects.get(pk=id_cidade)
    cidade.local = request.POST["local"]
    cidade.telefone = request.POST["telefone"]
    cidade.email = request.POST["email"]
    cidade.save()
    return redirect('cidades')