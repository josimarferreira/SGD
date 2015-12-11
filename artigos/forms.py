# coding utf-8

from django import forms
from .models import Artigos, Grupos


class ArtigosForm(forms.ModelForm):
    class Meta:
        model = Artigos
        fields = ['idartigos', 'idgrupo', 'descricao',]


class GruposForm(forms.ModelForm):
    class Meta:
        model = Grupos
        fields = ['idGrupos', 'grupo',]


