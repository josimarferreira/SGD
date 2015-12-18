# -*- coding: utf-8 -*-
from .models import Contatos
from django.contrib import admin

class ContatoAdmin(admin.ModelAdmin):
    model = Contatos
    list_display = ['contato_nome','contato_email','contato_site']
    list_filter = ['contato_sexo','contato_estado_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(Contatos, ContatoAdmin)
