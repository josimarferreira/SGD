# coding: utf-8
from django.conf.urls import url, patterns
from .views import AdicionaContato, ListaContatos, MostraContato, EditaContato, AdicionaEndereco, DeletaContato

urlpatterns = patterns('',
    url(r'^endereco(?P<nr_contato>\d+)/$', AdicionaEndereco, name='AdicionaEndereco'),
    url(r'^mostra(?P<nr_contato>\d+)/$', MostraContato, name='MostraContato'),
    url(r'^edita(?P<nr_contato>\d+)/$', EditaContato, name='EditaContato'),
    url(r'^deleta(?P<nr_contato>\d+)/$', DeletaContato, name='DeletaContato'),
    url(r'^novo/$', AdicionaContato, name='CriarContato'),
    url(r'^$', ListaContatos, name='lista'),
)
