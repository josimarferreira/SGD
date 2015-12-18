# coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .forms import ContatosForm
from .models import Contatos


def ListaContatos(request):
    lista = Contatos.objects.all()
    return render_to_response('contatos.html', {'lista': lista})


def AdicionaContato(request):
    if request.method == 'POST':
        form = ContatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = ContatosForm()
    return render_to_response('add_contato.html', {'form': form}, context_instance=RequestContext(request))


def MostraContato(request, nr_contato):
    contato = get_object_or_404(Contatos, pk=nr_contato)
    return render_to_response("mostra_contato.html", {'contato': contato})


def EditaContato(request, nr_contato):
    contato = get_object_or_404(Contatos, pk=nr_contato)
    if request.method == 'POST':
        form = ContatosForm(request.POST, request.FILES, instance=contato)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = ContatosForm(instance=contato)
    return render_to_response("edit_contato.html", {'form': form}, context_instance=RequestContext(request))



def DeletaContato(request, nr_contato):
    contato = get_object_or_404(Contatos, pk=nr_contato)
    form = ContatosForm(instance=contato)

    if request.method == 'POST':
        contato.delete()
        return render_to_response('deletado.html', {})
    else:
        return render_to_response("deletar.html", {'contato': contato}, RequestContext(request))

