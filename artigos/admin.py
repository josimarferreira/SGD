# -*- coding: utf-8 -*-
from .models import Artigos
from django.contrib import admin


class ArtigoAdmin(admin.ModelAdmin):
    model = Artigos
    list_display = ['idgrupo','descricao']
    list_filter = ['idgrupo']
    search_fields = ['descricao']
    save_on_top = True
admin.site.register(Artigos, ArtigoAdmin)
