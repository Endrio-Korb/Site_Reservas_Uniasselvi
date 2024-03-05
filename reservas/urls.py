from django.urls import path

from . import views
from .views import ReservarLabs

app_name = "reservas"

urlpatterns = [
    #path('laboratorio/',  views.ReservarLaboratorio, name='reservar_laboratorio'),
    path('modules/', views.modules, name='modules'),
    path('', views.registrarReservarLaboratorio, name='registrar_reserva'),

    
    path('reservas/', views.ReservarLabs.as_view(), name='reservar_laboratorio'),
]

