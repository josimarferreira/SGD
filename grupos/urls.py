# coding: utf-8
from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from .views import CreateGrupoView, ListaGrupos, ConsultaGrupo

urlpatterns = patterns('',
    url(r'^$', ListaGrupos.as_view(template_name='grupos.html'), name='lista'),
    url(r'^novo/$', CreateGrupoView.as_view(template_name='add_grupo.html'), name='add'),
    url(r'^consulta/$', ConsultaGrupo.as_view(template_name='consult_grupo.html'), name='consulta'),
)
