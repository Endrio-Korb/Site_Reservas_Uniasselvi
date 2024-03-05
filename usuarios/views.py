from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from django.urls import reverse_lazy


def login_user(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('consulta:consulta')
        else:
            erro = 'Usuário ou senha inválidos'
            return render(request, 'authenticate/login.html', {'erro':erro})
    else:
        return render(request,'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('Você saiu'))
    return redirect('consulta:consulta')


def cadastrar_user(request):
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

    user = User.objects.filter(username=usuario).first()

    if user:
        erro = 'Nome de usuário já está cadastrado'
        return render(request, 'cadastro.html', {'erro': erro})

    user = User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        is_staff=False,
    )
    user.groups.set('2')
    user.save()

    sucesso = 'Usuário cadastrado com sucesso'
    return render(request,'authenticate/login.html', {'sucesso':sucesso})