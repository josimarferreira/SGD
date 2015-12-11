# coding: utf-8

from django.db import models


class Contatos(models.Model):
    SEXO_CHOICES = (
        (u'1', u'Masculino'),
        (u'2', u'Feminino'),
    )
    ESTADO_CIVIL_CHOICES = (
        (u'1', u'Solteiro'),
        (u'2', u'Casado'),
        (u'3', u'Divorciado'),
        (u'4', u'Viúvo'),
    )
    contato_id = models.AutoField(primary_key=True)
    contato_nome = models.CharField(max_length=45, verbose_name='Nome')
    contato_nascimento = models.DateField(verbose_name='Data de Nascimento')
    contato_sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, verbose_name='Sexo')
    contato_estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
    #contato_foto = models.ImageField(max_length=255, blank=True, upload_to='contato/%Y', verbose_name='Foto')
    contato_email = models.EmailField(max_length=255, blank=True, verbose_name='Email')
    contato_site = models.URLField(max_length=255, blank=True, verbose_name='Site')
    contato_observacoes = models.TextField(blank=True, verbose_name='Observações')
    contato_favorito = models.BooleanField(verbose_name='Favorito')
    def __unicode__(self):
        return self.contato_nome
    class Meta:
        db_table = u'contatos'
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['contato_nome']


class Endereco(models.Model):
    TIPO_LOGRADOURO_CHOICES = (
        (u'rua', u'Rua'),
        (u'avenida', u'Avenida'),
        (u'travessa', u'Travessa'),
    )
    BAIRRO_CHOICES = (
        (u'Aerolândia ', u'Aerolândia '),
        (u'Aeroporto ', u'Aeroporto '),
        (u'José de Alencar (Antigo Alagadiço Novo) ',u'José de Alencar (Antigo Alagadiço Novo) '),
        (u'Aldeota ', u'Aldeota '),
        (u'Alto da Balança ', u'Alto da Balança '),
        (u'Álvaro Weyne ', u'Álvaro Weyne '),
        (u'Amadeu Furtado ', u'Amadeu Furtado '),
        (u'Ancuri ', u'Ancuri '),
        (u'Antônio Bezerra', u'Antônio Bezerra'),
        (u'Autran Nunes', u'Autran Nunes'),
        (u'Bairro De Lourdes', u'Bairro De Lourdes'),
        (u'Barra do Ceará', u'Barra do Ceará'),
        (u'Barroso', u'Barroso'),
        (u'Bela Vista', u'Bela Vista'),
        (u'Benfica', u'Benfica'),
        (u'Bom Futuro', u'Bom Futuro'),
        (u'Bom Jardim ', u'Bom Jardim '),
        (u'Bonsucesso ', u'Bonsucesso '),
        (u'Cais do Porto ', u'Cais do Porto '),
        (u'Cajazeiras ', u'Cajazeiras '),
        (u'Cambeba ', u'Cambeba '),
        (u'Canindezinho ', u'Canindezinho '),
        (u'Carlito Pamplona ', u'Carlito Pamplona '),
        (u'Castelão ', u'Castelão '),
        (u'Centro ', u'Centro '),
        (u'Cidade 2000 ', u'Cidade 2000 '),
        (u'Cidade dos Funcionários ', u'Cidade dos Funcionários '),
        (u'Coaçu ', u'Coaçu '),
        (u'Cocó ', u'Cocó '),
        (u'Conjunto Ceará ', u'Conjunto Ceará '),
        (u'Conjunto Esperança ', u'Conjunto Esperança '),
        (u'Conjunto São Miguel ', u'Conjunto São Miguel '),
        (u'Couto Fernandes ', u'Couto Fernandes '),
        (u'Cristo Redentor ', u'Cristo Redentor '),
        (u'Curió ', u'Curió '),
        (u'Damas ', u'Damas '),
        (u'Demócrito Rocha ', u'Demócrito Rocha '),
        (u'Dendê ', u'Dendê '),
        (u'Dionísio Torres ', u'Dionísio Torres '),
        (u'Dias Macêdo ', u'Dias Macêdo '),
        (u'Dom Lustosa ', u'Dom Lustosa '),
        (u'Dunas ', u'Dunas '),
        (u'Edson Queiroz ',u'Edson Queiroz '),
        (u'Ellery ',u'Ellery '),
        (u'Engenheiro Luciano Cavalcante ', u'Engenheiro Luciano Cavalcante '),
        (u'Farias Brito ', u'Farias Brito '),
        (u'Fátima ', u'Fátima '),
        (u'Floresta ', u'Floresta '),
        (u'Genibaú ', u'Genibaú '),
        (u'Granja Lisboa ', u'Granja Lisboa '),
        (u'Granja Portugal ', u'Granja Portugal '),
        (u'Guajerú ', u'Guajerú '),
        (u'Henrique Jorge ', u'Henrique Jorge '),
        (u'Itaóca ', u'Itaóca '),
        (u'Itaperi ', u'Itaperi '),
        (u'Jacarecanga', u'Jacarecanga'),
        (u'Jangurussu[4] ', u'Jangurussu[4] '),
        (u'Jardim América ', u'Jardim América '),
        (u'Jardim Cearense ', u'Jardim Cearense '),
        (u'Jardim das Oliveiras ', u'Jardim das Oliveiras '),
        (u'Jardim Guanabara ', u'Jardim Guanabara '),
        (u'Jardim Iracema ', u'Jardim Iracema '),
        (u'João XXIII ', u'João XXIII '),
        (u'Joaquim Távora ', u'Joaquim Távora '),
        (u'Jóquei Clube ', u'Jóquei Clube '),
        (u'José Bonifácio ', u'José Bonifácio '),
        (u'Lagoa Redonda ', u'Lagoa Redonda '),
        (u'Manuel Sátiro ', u'Manuel Sátiro '),
        (u'Maraponga ', u'Maraponga '),
        (u'Mata Galinha ', u'Mata Galinha '),
        (u'Meireles ', u'Meireles '),
        (u'Messejana ', u'Messejana '),
        (u'Mondubim ', u'Mondubim '),
        (u'Monte Castelo ', u'Monte Castelo '),
        (u'Montese ', u'Montese '),
        (u'Moura Brasil ', u'Moura Brasil '),
        (u'Mucuripe ', u'Mucuripe '),
        (u'Novo Mondubim ', u'Novo Mondubim '),
        (u'Olavo Oliveira ', u'Olavo Oliveira '),
        (u'Padre Andrade ', u'Padre Andrade '),
        (u'Panamericano ', u'Panamericano '),
        (u'Papicu ', u'Papicu '),
        (u'Parangaba ', u'Parangaba '),
        (u'Parque Araxá ', u'Parque Araxá '),
        (u'Parque Dois Irmãos ', u'Parque Dois Irmãos '),
        (u'Parque Iracema ', u'Parque Iracema '),
        (u'Parque Manibura ', u'Parque Manibura '),
        (u'Parque Santa Maria ', u'Parque Santa Maria '),
        (u'Parque Santa Rosa ',u'Parque Santa Rosa '),
        (u'Parquelândia ', u'Parquelândia '),
        (u'Parreão ', u'Parreão '),
        (u'Passaré ', u'Passaré '),
        (u'Patriolino Ribeiro ', u'Patriolino Ribeiro '),
        (u'Paupina ', u'Paupina '),
        (u'Pedras ', u'Pedras '),
        (u'Planalto Ayrton Senna (antigo Pantanal) ', u'Planalto Ayrton Senna (antigo Pantanal) '),
        (u'Pici ', u'Pici '),
        (u'Pirambu ', u'Pirambu '),
        (u'Praia de Iracema ', u'Praia de Iracema '),
        (u'Praia do Futuro I ', u'Praia do Futuro I '),
        (u'Praia do Futuro II ', u'Praia do Futuro II '),
        (u'Prefeito José Walter ', u'Prefeito José Walter '),
        (u'Presidente Kennedy ', u'Presidente Kennedy '),
        (u'Presidente Vargas ', u'Presidente Vargas '),
        (u'Quintino Cunha ', u'Quintino Cunha '),
        (u'Rodolfo Teófilo ',u'Rodolfo Teófilo '),
        (u'Sabiaguaba ', u'Sabiaguaba '),
        (u'Salinas ', u'Salinas '),
        (u'São Bento ', u'São Bento '),
        (u'São Gerardo ', u'São Gerardo '),
        (u'São João do Tauape ', u'São João do Tauape '),
        (u'Parque São José ', u'Parque São José '),
        (u'Sapiranga ', u'Sapiranga '),
        (u'Serrinha ', u'Serrinha '),
        (u'Siqueira ', u'Siqueira '),
        (u'Varjota ', u'Varjota '),
        (u'Vicente Pinzón ', u'Vicente Pinzón '),
        (u'Vila Pery ', u'Vila Pery '),
        (u'Vila União ', u'Vila União '),
        (u'Vila Velha ', u'Vila Velha '),
    )
    endereco_id = models.AutoField(primary_key=True)
    contato = models.ForeignKey(Contatos)
    endereco_tipo_logradouro = models.CharField(max_length=10, choices=TIPO_LOGRADOURO_CHOICES, verbose_name='Tipo Logradouro')
    endereco_logradouro = models.CharField(max_length=80, verbose_name='Logradouro')
    endereco_numero = models.IntegerField(verbose_name='Número')
    endereco_complemento = models.CharField(max_length=45, blank=True, verbose_name='Complemento')
    endereco_bairro = models.CharField(max_length=80, verbose_name='Bairro', choices=BAIRRO_CHOICES)
    endereco_cidade = models.CharField(max_length=80, default='Fortaleza')
    endereco_estado = models.CharField(max_length=2, verbose_name='Estado', default='Ceará')
    endereco_cep = models.CharField(max_length=9, blank=True, verbose_name='CEP')

    def __unicode__(self):
        return '%s %s, %s, %s, %s - %s' % (self.endereco_tipo_logradouro, self.endereco_logradouro, self.endereco_numero, self.endereco_bairro, self.endereco_cidade, self.endereco_estado)

    class Meta:
        db_table = u'endereco'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['endereco_bairro']


class Telefone(models.Model):
    TELEFONE_TIPO_CHOICES = (
        (u'1', u'Residencial'),
        (u'2', u'Celular'),
        (u'3', u'Comercial'),
    )
    telefone_id = models.AutoField(primary_key=True)
    contato = models.ForeignKey(Contatos)
    telefone_tipo = models.CharField(max_length=15, choices=TELEFONE_TIPO_CHOICES, verbose_name='Tipo')
    telefone_numero = models.CharField(max_length=13, verbose_name='Número')

    def __unicode__(self):
        return self.telefone_numero

    class Meta:
        db_table = u'telefone'
