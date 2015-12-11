# coding: utf-8
from django.conf.urls import include, url, patterns
from django.views.generic import TemplateView
from .views import CreateDoacoesView

urlpatterns = patterns('',
    url(r'^novo/$', CreateDoacoesView.as_view(), name='CriarDoacao'),
    url(r'^$', TemplateView.as_view(template_name='doacoes.html'), name='doacoes'),
)

