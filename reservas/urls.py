from django.urls import path

from . import views
from .views import ReservarLabs, Editar, CancelarReserva

app_name = "reservas"

urlpatterns = [
    #path('laboratorio/',  views.ReservarLaboratorios, name='reservar_laboratorio'),
    path('modules/', views.modules, name='modules'),
    path('', views.registrarReservarLaboratorio, name='registrar_reserva'),

    
    path('reservas/', views.ReservarLabs.as_view(), name='reserva_form'),
    path('editar/<int:pk>', Editar.as_view(), name='editar'),
    path('reservas/<int:pk>/cancelar/', CancelarReserva.as_view(), name='cancelar'),
]

