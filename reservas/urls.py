from django.urls import path

from . import views
from .views import ReservarLabs, Editar, cancelar, editar

app_name = "reservas"

urlpatterns = [
    path('modules/', views.modules, name='modules'),
    path('', views.registrarReservarLaboratorio, name='registrar_reserva'),

    
    path('reservas/', views.ReservarLabs.as_view(), name='reserva_form'),

    #path('editar/<int:pk>', Editar.as_view(), name='editar'),
    path('reservas/<int:pk>/editar', editar, name='editar'),

    path('reservas/<int:pk>/cancelar/', cancelar, name='cancelar')
]

