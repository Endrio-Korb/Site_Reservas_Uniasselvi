from django.urls import path

from . import views

app_name = "reservas"

urlpatterns = [
    path('laboratorio/',  views.ReservarLaboratorio, name='reservar_laboratorio'),
    path('modules/', views.modules, name='modules'),
    path('', views.registrarReservarLaboratorio, name='registrar_reserva'),
]

