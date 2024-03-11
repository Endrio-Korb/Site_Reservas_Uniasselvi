from django.db.models.query import QuerySet
from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos
from professores.models import Professores
from django.contrib.auth.models import User, Group

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from django.contrib import messages
from braces.views import GroupRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


class ReservarLabs(GroupRequiredMixin, ListView):
    group_required = u'Funcionarios'
    model = Blocos
    queryset = Blocos.objects.all()
    template_name = 'reserva_labs.html'


def modules(request):
    bloco = request.GET.get('blocos')

    professores = Professores.objects.all()
    laboratorios = Laboratorios.objects.filter(bloco_id=bloco)
    periodos = Periodos.objects.all()

    contexto = {'laboratorios': laboratorios,
                'periodos':periodos,
                 'professores':professores}
    return render(request, 'partials/modules.html', contexto)


def registrarReservarLaboratorio(request):
    blocos = Blocos.objects.all()
    
    if request.method == 'POST':
        bloco = request.POST.get('blocos')
        data = request.POST.get('data')
        periodo = request.POST.get('periodo')
        lab = request.POST.get('nome_lab')
        professor = request.POST.get('nome_professor')

        professor = professor.lower()
        professor = professor.title()

        if bloco == 'Selecione o Bloco':
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if data == "":
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if periodo == 'Selecione o Periodo':
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if lab == 'Selecione o Laboratório':
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if professor == "":
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
    
        

        if not Professores.objects.filter(nome=professor):
            salva_nome_professor = Professores.objects.create(
            nome = f'{professor}')
            salva_nome_professor.save()

        verificar_reserva = ReservasLaboratorios.objects.filter(laboratorio=lab).filter(data_reserva=data).filter(bloco_id=bloco).filter(periodo_id=periodo).only('laboratorio')

        if verificar_reserva:
            nome_lab = Laboratorios.objects.get(id=lab)
            str_periodo = Periodos.objects.get(id=periodo)
            erro = f'{nome_lab.nome} já está reservado no periodo {str_periodo} para data {data} '
            return render(request, 'consulta.html', {'blocos':blocos,
                                                     'erro':erro})
        
        else:
            reserva = ReservasLaboratorios.objects.create(
                data_reserva = f'{data}',
                professor = Professores.objects.get(nome=professor),
                periodo_id = f'{periodo}',
                laboratorio = Laboratorios.objects.get(id=lab),
                bloco_id = f'{bloco}',
            )
            reserva.save()
            sucesso = 'Reserva registrada com sucesso'
            return render(request, 'consulta.html', {'blocos': blocos,
                                                      'sucesso': sucesso})


# Editar uma tabela do bando de dados
class Editar(GroupRequiredMixin, UpdateView):
    group_required = u'Funcionarios'
    model = ReservasLaboratorios
    fields= ('professor', 'data_reserva')
    template_name = 'editar.html'
    context_object_name = 'reserva'
    success_url = reverse_lazy('consulta:consulta')
    sucesso = 'Reserva atualizada com sucesso'
    

# Apagar uma reserva do banco de dados
class CancelarForm(GroupRequiredMixin, DeleteView):
    group_required = u'Funcionarios'
    model = ReservasLaboratorios
    context_object_name = 'reserva'
    template_name = 'cancelar.html'
    success_url = reverse_lazy('consulta:consulta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sucesso"] = 'Reserva cancelada com sucesso'
        return context
    



# def is_funcionario(user):
#     return user.groups.filter(name='Funcionarios').exists()


def editar_form(request, pk):
    usuario = request.user
    if usuario.groups.filter(name='Funcionarios').exists():
        reserva = ReservasLaboratorios.objects.get(pk=pk)
        return render(request, 'editar.html', {'reserva':reserva})
    else:
        erro = 'Ocorreu algum problema ou você não tem permissão para acessar essa página'
        return render(request,'editar.html', {'erro':erro})
    
def editar(request, pk):
    
    if request.method == 'GET':
        professor = request.POST.get('professor')
        data = request.POST.get('data')

        if not professor == None or not data == None:
            ReservasLaboratorios.objects.filter(pk=pk).update(professor=professor).update(data_reserva=data)
            sucesso = "Reserva atualizada com sucesso"
            return render(request, 'consulta.html', {'sucesso':sucesso})
        
    else:
        aviso = 'Prencha todos os campos'
        pk = pk
        return render(request, 'editar.html', {'aviso':aviso,
                                               'pk': pk})
    