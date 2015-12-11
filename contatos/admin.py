# -*- coding: utf-8 -*-
from .models import Contatos, Endereco, Telefone
from django.contrib import admin

class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 3
class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1
class ContatoAdmin(admin.ModelAdmin):
    model = Contatos
    list_display = ['contato_nome','contato_email','contato_site']
    list_filter = ['contato_sexo','contato_estado_civil']
    search_fields = ['contato_nome']
    inlines = [TelefoneInline, EnderecoInline]
    save_on_top = True
admin.site.register(Contatos, ContatoAdmin)
