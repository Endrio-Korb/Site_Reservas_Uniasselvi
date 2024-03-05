from django.urls import path
from .views import (login_user, cadastrar_user, logout_user)

app_name = 'usuarios'

urlpatterns = [
    #path('cadastro/', cadastro.a(), name='cadastro'),
    path('login/', login_user, name='login'),
    path('cadastrar/', cadastrar_user, name='cadastrar'),
    path('logout/', logout_user, name='logout'),
]
