# coding: utf-8
from django import forms
from doacoes.models import Doacoes


class DoacoesForm(forms.ModelForm):
    class Meta:
        model = Doacoes
        fields = ['doacoes_id', 'doacoes_data', 'doacoes_doador', 'doacoes_status']

