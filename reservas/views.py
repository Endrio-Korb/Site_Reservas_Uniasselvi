from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos
from professores.models import Professores
from django.contrib.auth.models import User


from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from braces.views import GroupRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView



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
        
class Editar(UpdateView):
    model = ReservasLaboratorios
    fields = ('laboratorio', 'data_reserva', 'bloco', 'periodo', 'professor')
    template_name = 'editar.html'
    success_url = reverse_lazy('editar')

    def form_valid(self, form):
        messages.success(self.request,'Sucesso')
        return super(Editar, self).form_valid(form)
    


class CancelarForm(GroupRequiredMixin, ListView):
    pk = 16
    group_required = u'Funcionarios'
    model = ReservasLaboratorios
    queryset = ReservasLaboratorios.objects.get(pk=pk)
    template_name = 'cancelar.html'

def cancelar(request, pk):
    reserva = get_object_or_404(ReservasLaboratorios, pk=pk)
    reserva.delete()
    sucesso = "Reserva Cancelada"
    blocos = Blocos.objects.all()
    return render(request, 'consulta.html', {'sucesso':sucesso,
                                             'blocos':blocos})


def editar(request, pk):
    texto = ReservasLaboratorios.objects.get(pk=pk)
    editar = ReservasLaboratorios.objects.get(pk=pk)

    return render(request, 'editar.html', {'texto':texto,
                                           'editar':editar})
    