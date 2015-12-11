# coding utf-8

from django import forms
from .models import Contatos, Endereco


class ContatosForm(forms.ModelForm):
    class Meta:
        model = Contatos
        fields = '__all__'


class EnderecoForm(forms.Form):
    class Meta:
        model = Endereco
        fields = '__all__'