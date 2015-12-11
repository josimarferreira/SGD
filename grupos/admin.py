# -*- coding: utf-8 -*-
from .models import Grupos
from artigos.models import Artigos
from django.contrib import admin


#class ArtigoInline(admin.TabularInline):
#    model = Artigos
#    extra = 3


class GruposAdmin(admin.ModelAdmin):
    model = Grupos
    list_display = ['idgrupo', 'grupo']
    list_filter = ['grupo']
    search_fields = ['grupo']
#    inline = [ArtigoInline]
    save_on_top = True


admin.site.register(Grupos)#, ArtigoInline)
