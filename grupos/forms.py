# coding utf-8

from django import forms
from .models import Grupos


class GruposForm(forms.ModelForm):

    class Meta:
        model = Grupos
        fields = ['idGrupos', 'grupo', ]