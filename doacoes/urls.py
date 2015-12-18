# coding: utf-8

from django.conf.urls import include, url, patterns
from .views import AdicionaDoacao, MostraDoacao, EditaDoacao, DeletaDoacao, ListaDoacoes

urlpatterns = patterns('',
    url(r'^novo/$', AdicionaDoacao, name='CriarDoacao'),
    url(r'^mostra(?P<nr_contato>\d+)/$', MostraDoacao, name='MostraDoacao'),
    url(r'^edita(?P<nr_contato>\d+)/$', EditaDoacao, name='EditaDoacao'),
    url(r'^deleta(?P<nr_contato>\d+)/$', DeletaDoacao, name='DeletaDoacao'),
    url(r'^$', ListaDoacoes, name='lista'),
)
