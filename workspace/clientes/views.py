from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cliente_detail(request, id):
    return HttpResponse(id)

def cliente_por_nome(request, nome):
    return HttpResponse(f"Olá, {nome}")

def clientes(request):
    return HttpResponse("Maria , João e Madalena")