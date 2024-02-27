from django.shortcuts import render, HttpResponse

from reservas.models import ReservasLaboratorios, Laboratorios, Blocos

from django.db.models import Value as V
from django.db.models import Q
from django.db.models.functions import Concat
from django import forms

from datetime import datetime

def consulta(request):
    blocos = Blocos.objects.all()
    return render(request, "consulta.html", {'blocos':blocos})


def mostrarEnsalamentoLabs(request):

    if request.method=="POST":
            
        bloco = request.POST.get('bloco')
        data = request.POST.get('data')
        
        if (not data) or (not bloco.isdigit()):

            erro = 'Data ou Bloco faltando'
            blocos = Blocos.objects.all()
            return render(request, 'consulta.html', {'erro':erro,
                                                    'blocos':blocos})
        else:
            nome_bloco = Blocos.objects.get(id_bloco=bloco)
            labs_reservados = ReservasLaboratorios.objects.filter(data_reserva=data).filter(bloco=bloco).order_by('laboratorio')
    
            todos_labs = Laboratorios.objects.filter(bloco=bloco)
            labs_disponiveis = []
            for lab in todos_labs:
                if not ReservasLaboratorios.objects.filter(laboratorio=lab).filter(data_reserva=data).filter(bloco=bloco):
                    labs_disponiveis.append(f'{lab.nome} {lab.bloco}{lab.numero_sala}')

            return render(request, 'ensalamento_labs.html', {'labs_disponiveis': labs_disponiveis,
                                                            'labs_reservados':labs_reservados,
                                                            'data':data,
                                                            'nome_bloco':nome_bloco,
                                                            'todos_labs':todos_labs})


def mostrarEnsalamentoLabsNome(request):

    data = request.POST.get('data')
    nome_prof = request.POST.get('nome_professor')
    nome_prof = nome_prof.upper()

    if not data or not nome_prof:
        blocos = Blocos.objects.all()
        mensagem = 'Data ou nome do professor faltando'
        return render(request, 'consulta.html', {'mensagem':mensagem,
                                                 'blocos':blocos})

    labs_reservados = ReservasLaboratorios.objects.annotate(full_name=Concat('nome_professor', V(' '))).filter(full_name__icontains=nome_prof).filter(data_reserva=data).order_by('nome_laboratorio')

    if labs_reservados:
        return render(request, 'ensalamento_labs_nome.html', {'labs_reservados': labs_reservados,
                                                            'data': data})
    else:
        mensagem = 'Não há laboratórios reservados para esse professor(a)'
        return render(request, 'ensalamento_labs_nome.html', {'mensagem':mensagem})
