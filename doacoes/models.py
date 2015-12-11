# coding utf-8
from django.db import models
from artigos.models import Artigos
from contatos.models import Contatos

class Doacoes(models.Model):
    STATUS_CHOICES = (
        (u'1', u'Pendente'),
        (u'2', u'Em andamento'),
        (u'3', u'Coleta realizada'),
        (u'4', u'Outros'),
    )
    iddoacoes = models.AutoField(db_column='idDoacoes', primary_key=True)  # Field name made lowercase.
    iddoador = models.ForeignKey(Contatos, db_column='idDoador', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    qt_itens = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doacoes'

class Itens(models.Model):
    iddoacao = models.ForeignKey(Doacoes, db_column='idDoacao')  # Field name made lowercase.
    idartigo = models.ForeignKey(Artigos, db_column='idArtigo')  # Field name made lowercase.
    quantidade = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itens'
