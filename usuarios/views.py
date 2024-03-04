from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmaca_senha = request.POST.get('confirmacao_senha')

    if not senha == confirmaca_senha:
        erro = 'As senhas não conferem'
        return render(request,'cadastro.html', {'erro': erro})
        


def login(request):
    return render(request, 'login.html')