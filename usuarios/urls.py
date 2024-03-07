from django.urls import path
from .views import (login_user, cadastrar_user, logout_user)
from .views import UsuarioUpdate, Usuarios

app_name = 'usuarios'

urlpatterns = [
    #path('cadastro/', cadastro.a(), name='cadastro'),
    path('login/', login_user, name='login'),
    path('cadastrar/', cadastrar_user, name='cadastrar'),
    path('logout/', logout_user, name='logout'),
    path('dados', Usuarios.as_view(), name='dados'),
    path('atualizar-dados', UsuarioUpdate.as_view(), name='atualizar'),
]
