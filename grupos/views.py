# coding: utf-8
from django.views.generic import TemplateView, ListView
from django.shortcuts import redirect, render

from .forms import GruposForm
from grupos.models import Grupos


class CreateGrupoView(TemplateView):
    template_name = ['grupos.html', 'add_grupo.html', ]

    def get_context_data(self, **kwargs):
        context = super(CreateGrupoView, self).get_context_data(**kwargs)
        context['form'] = GruposForm(self.request.POST or None)
        return context

    def post(self, request):
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            form.save()
            return redirect('grupos')
        return self.render_to_response(context)


class ListaGrupos(ListView):
    template_name = 'grupos.html'
    model = Grupos
    context_object_name = 'grupo'

class ConsultaGrupo(TemplateView):
    template_name = 'consult_grupo.html'
    model = Grupos
    context_object_name = 'grupo'
