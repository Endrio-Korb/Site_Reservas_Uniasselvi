from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django


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
    user.save()

    sucesso = 'Usuário cadastrado com sucesso'
    return render(request,'login.html', {'sucesso':sucesso})
        


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        usuario = request.POST.get = ('usuario')
        senha = request.POST.get = ('senha')

        user = authenticate(username=usuario, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'consulta.html')
        else:
            erro = 'Usuário ou senha inválidos'
            return render(request,'login.html', {'erro': erro})
