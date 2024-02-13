from django.contrib import admin

from .models import Laboratorios, ReservasLaboratorios, Status, Blocos, Periodos
admin.site.register(Laboratorios)
admin.site.register(ReservasLaboratorios)
admin.site.register(Status)
admin.site.register(Blocos)
admin.site.register(Periodos)