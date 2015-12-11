# coding: utf-8
from django.db import models
from grupos.models import Grupos


class Artigos(models.Model):
    idartigos = models.AutoField(db_column='idArtigos', primary_key=True, verbose_name='Código')  # Field name made lowercase.
    idgrupo = models.ForeignKey(Grupos, db_column='idgrupo', blank=False, null=False, verbose_name='Grupo')  # Field name made lowercase.
    descricao = models.CharField(max_length=70, blank=True, null=True,verbose_name='Descrição')

    class Meta:
        managed = False
        db_table = 'artigos'


