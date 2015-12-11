# coding: utf-8

from django.db import models

class Grupos(models.Model):
    idGrupos = models.AutoField(db_column='idGrupos', primary_key=True)
    grupo = models.CharField(max_length=70, help_text='Nome do grupo sem abreviações')


    class Meta:
        managed = False
        db_table = 'grupos'

    def __unicode__(self):
        return self.grupo

