# coding: utf-8
from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from .views import CreateArtigoView, ListaArtigos

urlpatterns = patterns('',
    url(r'^novo/$', CreateArtigoView.as_view(), name='CriarArtigo'),
    url(r'^$', ListaArtigos.as_view(template_name='artigos.html'), name='lista'),
)
