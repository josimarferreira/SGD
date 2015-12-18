# coding: utf-8
from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404, render_to_response
from .forms import DoacoesForm
from .models import Doacoes


def ListaDoacoes(request):
    lista = Doacoes.objects.all()
    return render_to_response('doacoes.html',  {'lista': lista})


def AdicionaDoacao(request):
    if request.method == 'POST':
        form = DoacoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = DoacoesForm()
    return render_to_response('add_doacao.html', {'form': form}, context_instance=RequestContext(request))


def EditaDoacao(request, nr_contato):
    doacao = get_object_or_404(Doacoes, pk=nr_contato)
    if request.method == 'POST':
        form = DoacoesForm(request.POST, request.FILES, instance=doacao)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = DoacoesForm(instance=doacao)
    return render_to_response('edita_doacao.html', {'form': form}, context_instance=RequestContext(request))



def DeletaDoacao(request, nr_contato):
    doacao = get_object_or_404(Doacoes, pk=nr_contato)
    form = Doacoes(instance=doacao)

    if request.method == 'POST':
        doacao.delete()
        return render_to_response('doacao_deletada.html', {})
    else:
        return render_to_response('deleta_doacao.html', {'doacao': doacao}, RequestContext(request))


def MostraDoacao(request, nr_contato):
    doacao = get_object_or_404(Doacoes, pk=nr_contato)
    return render_to_response('mostra_doacao.html', {'artigo': doacao})

