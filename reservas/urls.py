from django.urls import path


from .views import ReservarLabs, CancelarForm
from .views import editar_form, registrarReservarLaboratorio, modules, editar

app_name = "reservas"

urlpatterns = [
    path('reservas/', ReservarLabs.as_view(), name='reserva_form'),    
    path('<int:pk>/cancelar', CancelarForm.as_view(), name='cancelar_form'),

    
    path('', registrarReservarLaboratorio, name='registrar_reserva'),
    path('modules/', modules, name='modules'),

    #path('<int:pk>/editar', Editar.as_view(), name='editar'),
    path('<int:pk>/editar_form', editar_form, name='editar_form'),
    path('<int:pk>/editar', editar, name='editar'),
]

