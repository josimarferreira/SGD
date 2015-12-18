# coding utf-8

from django import forms
from .models import Contatos


class ContatosForm(forms.ModelForm):
    class Meta:
        model = Contatos
        fields = '__all__'

