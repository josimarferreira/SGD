# coding: utf-8

from django.db import models
from contatos.models import Contatos
from artigos.models import Artigos

class Doacoes(models.Model):
    STATUS_CHOICES = (
        (u'1', u'Não coletado'),
        (u'2', u'Coleta em andamento'),
        (u'3', u'Coletado'),
    )
    doacoes_id = models.AutoField(primary_key=True)
    doacoes_data = models.DateField(verbose_name=u'Data da doação')
    doacoes_doador = models.ForeignKey(Contatos, db_column='doacoes_doador', blank=False, null=False, verbose_name=u'Doador')
    doacoes_status = models.CharField(verbose_name=u'Status', choices=STATUS_CHOICES, max_length=1)


    class Meta:
        managed = False
        db_table = 'doacoes'


class Itens(models.Model):
    UNID_MEDIDA_CHOICES = (
        (u'1', u'Unitário'),
        (u'2', u'Conjunto'),
        (u'3', u'Kg - Kilograma'),
        (u'3', u'm - Metro'),
        (u'3', u'L - Litro'),
    )
    doacao_id = models.ForeignKey(Doacoes, db_column='doacoes_id', blank=False, null=False, verbose_name= u'Código da Doação')
    doacao_artigo = models.ForeignKey(Artigos, db_column='idartigos', blank=False, null=False, verbose_name= u'Artigo doado')
    doacao_unid_medida = models.CharField(verbose_name= u'Unidade de medida', max_length=20, choices=UNID_MEDIDA_CHOICES)
    doacao_quantidade = models.IntegerField(verbose_name= u'Quantidade doada')
    doacao_status = models.CharField(verbose_name= u'Status', max_length=1)


    class Meta:
        managed = False
        db_table = 'itens'

    def __str__(self):
        return self.doacao_artigo, self.doacao_unid_medida, self.doacao_quantidade, self.doacao_status
