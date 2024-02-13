from django import forms

from .models import Laboratorios, Blocos


class LocationForm(forms.Form):
    bloco = forms.ModelChoiceField(queryset=Blocos.objects.all())
    laboratorio = forms.ModelChoiceField(queryset=Laboratorios.objects.none())