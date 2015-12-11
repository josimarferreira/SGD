# coding: utf-8

from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from artigos.forms import ArtigosForm
from artigos.models import Artigos


class CreateArtigoView(TemplateView):
    template_name = 'add_artigo.html'

    def get_context_data(self, **kwargs):
        context = super(CreateArtigoView, self).get_context_data(**kwargs)
        context['form'] = ArtigosForm(self.request.POST or None)
        return context

    def post(self, request):
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            form.save()
            return redirect('artigos.html')
        return self.render_to_response(context)


class ListaArtigos(ListView):
    template_name = 'artigos.html'
    model = Artigos
    context_object_name = 'artigo'
