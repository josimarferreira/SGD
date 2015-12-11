# coding: utf-8

from django.views.generic import TemplateView
from django.shortcuts import render


class CreateDoacoesView(TemplateView):
    template_name = 'create.html'