# coding: utf-8
from django.template import RequestContext

from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .forms import ArtigosForm
from .models import Artigos


class ListaArtigos(ListView):
    template_name = 'artigos.html'
    model = Artigos
    context_object_name = 'artigo'


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


def EditaArtigo(request, nr_contato):
    artigo = get_object_or_404(Artigos, pk=nr_contato)
    if request.method == 'POST':
        form = ArtigosForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = ArtigosForm(instance=artigo)
    return render_to_response("edita_artigo.html", {'form': form}, context_instance=RequestContext(request))



def DeletaArtigo(request, nr_contato):
    artigo = get_object_or_404(Artigos, pk=nr_contato)
    form = ArtigosForm(instance=artigo)

    if request.method == 'POST':
        artigo.delete()
        return render_to_response('artigo_deletado.html', {})
    else:
        return render_to_response("deleta_artigo.html", {'artigo': artigo}, RequestContext(request))


def MostraArtigo(request, nr_contato):
    artigo = get_object_or_404(Artigos, pk=nr_contato)
    return render_to_response("mostra_artigo.html", {'artigo': artigo})



