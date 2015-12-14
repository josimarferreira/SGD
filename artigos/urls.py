# coding: utf-8
from django.conf.urls import include, url, patterns
from .views import CreateArtigoView, ListaArtigos, MostraArtigo, DeletaArtigo, EditaArtigo

urlpatterns = patterns('',
    url(r'^novo/$', CreateArtigoView.as_view(), name='CriarArtigo'),
    url(r'^mostra(?P<nr_contato>\d+)/$', MostraArtigo, name='MostraArtigo'),
    url(r'^edita(?P<nr_contato>\d+)/$', EditaArtigo, name='EditaArtigo'),
    url(r'^deleta(?P<nr_contato>\d+)/$', DeletaArtigo, name='DeletaArtigo'),
    url(r'^$', ListaArtigos.as_view(template_name='artigos.html'), name='lista'),
)
