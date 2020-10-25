from django.db import models
from datetime import date


# Create your models here.


class Telefone(models.Model):
    TELEFONE = models.CharField(max_length=20)

    class Meta:
        db_table = 'Telefone'

    def __str__(self):
        return self.TELEFONE


class Cliente(models.Model):
    NOME = models.CharField(max_length=100)
    PFPJOP = (
        ('F', 'Física'),
        ('J', 'Jurídica'),
    )
    PFPJ = models.CharField(max_length=1, choices=PFPJOP, verbose_name='FÍSICA OU JURÍDICA')
    CPFCNPJ = models.CharField(blank=True, null=True, max_length=20, verbose_name='CPF/CNPJ')
    EMAIL1 = models.CharField(max_length=60, blank=True, null=True)
    EMAIL2 = models.CharField(max_length=60, blank=True, null=True)
    DATAHORACADASTRO = models.DateTimeField(auto_now=True)
    TELEFONE = models.ManyToManyField(Telefone)
    LOCAL = 0
    SALVARCLIENTE = 'salvar'
    CONTATO = 0

    class Meta:
        db_table = 'Cliente'

    def setLocal(self, l):
        self.LOCAL = l

    def getLocal(self):
        return Local.objects.get(id=self.LOCAL)

    def getLocais(self):
        return Local.objects.filter(ID_CLIENTE=self.id)

    def getSalvarCliente(self):
        return self.SALVARCLIENTE

    def setSalvarCliente(self, l):
        self.SALVARCLIENTE = l

    def setContato(self, c):
        self.CONTATO = c

    def getUfSeletec(self, uf):
        l = self.getLocal()
        if uf == l.ESTADO:
            return 'Selected'
        else:
            return ''

    def getContato(self):
        return Contato.objects.get(id=self.CONTATO)

    def getContatos(self):
        return Contato.objects.filter(ID_CLIENTE=self.id)

    def getTelefonesContatos(self):
        ctt = Contato.objects.get(id=self.CONTATO)
        return ctt.TELEFONE.all()

    def __str__(self):
        return self.NOME

    def getNome(self):
        return self.NOME


class Conta(models.Model):
    DESCRICAO = models.CharField(max_length=100, verbose_name='DESCRIÇÃO')
    BANCO = models.IntegerField(blank=True, null=True)
    AGENCIA = models.CharField(max_length=15, blank=True, null=True, verbose_name='AGÊNCIA')
    CONTA = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'Conta'

    def __str__(self):
        return self.DESCRICAO


class Funcionario(models.Model):
    NOME = models.CharField(max_length=100)
    EMAIL = models.CharField(null=True, blank=True, max_length=50)
    DATA_NASCIMENTO= models.DateField(blank=False, null=False)
    TELEFONE = models.ManyToManyField(Telefone)

    class Meta:
        db_table = 'Funcionário'

    def __str__(self):
        return self.NOME

    def getDATA_NASCIMENTO(self):
        return self.DATA_NASCIMENTO.strftime('%Y-%m-%d')


class Local(models.Model):
    CEP = models.CharField(max_length=20)
    LOGRADOURO = models.CharField(max_length=100)
    NUMERO = models.CharField(max_length=10, verbose_name='NÚMERO')
    BAIRRO = models.CharField(max_length=70, blank=True, null=True)
    CIDADE = models.CharField(max_length=50, blank=True, null= True)
    ESTADO_lista = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RD', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal'),
    )
    ESTADO = models.CharField(max_length=2, blank=True, null=True, choices=ESTADO_lista)
    REFERENCIA = models.CharField(null=True, blank=True, max_length=100, verbose_name='PONTO DE REFERÊNCIA')
    COORDENADAS = models.CharField(null=True, blank=True, max_length=100, verbose_name='COORDENADAS DE LOCALIZAÇÃO')
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='CLIENTE')
    AREA = models.CharField(null=True, blank=True, max_length=100, verbose_name='ÁREA TOTAL')
    COMPARTIMENTOS = models.IntegerField(null=True, blank=True, verbose_name='NÚMERO DE COMPARTIMENTOS')
    BANHEIROS = models.CharField(null=True, blank=True, max_length=100, verbose_name='NÚMERO DE BANHEIROS')
    OBS = models.CharField(null=True, blank=True, max_length=200, verbose_name='OBSERVAÇÕES')

    class Meta:
        db_table = 'Local'

    def __str__(self):
        return self.LOGRADOURO + ' ' + self.NUMERO


class Produto(models.Model):
    DESCRICAO = models.CharField(max_length=100, verbose_name='DESCRIÇÃO')
    UND = (
        ('UND', 'Unidade'),
        ('KG', 'Kilograma'),
        ('ML', 'Mililitros'),
        ('L', 'Litros'),
        ('UND', 'Unidade'),
        ('KG', 'Kilograma'),
    )

    UNIDADE = models.CharField(max_length=3, choices=UND, verbose_name='UNIDADE')
    ESTOQUEMINIMO = models.IntegerField(verbose_name='ESTOQUE MÍNIMO')
    INSTRUCOES = models.CharField(null=True, blank=True, max_length=200, verbose_name='INSTRUÇÕES DE PREPARO')
    TIPOLST = (
        ('Equipamento', ''),
        ('Veneno', ''),
        ('Químico', ''),
        ('Diluente', ''),
    )
    TIPO = models.CharField(choices=TIPOLST, max_length=20, verbose_name='TIPO DE PRODUTO')

    class Meta:
        db_table = 'Produto'

    def __str__(self):
        return self.DESCRICAO


class Servico(models.Model):
    DESCRICAO = models.CharField(max_length=100, verbose_name='DESCRIÇÃO')
    RECOMENDACOES = models.CharField(null=True, blank=True, max_length=100, verbose_name='RECOMENDAÇÕES')
    VALOR1 = models.FloatField(verbose_name='VALOR 1')
    VALOR2 = models.FloatField(verbose_name='VALOR 2')
    VALOR3 = models.FloatField(verbose_name='VALOR 3')
    DESCONTOPERMITIDO = models.FloatField(verbose_name='LIMITE PARA DESCONTO (%)')
    LIMITEAREA = models.FloatField(verbose_name='LIMITE PARA ÁREA(m²)')
    LIMITECOMPARTIMENTOS = models.IntegerField(verbose_name='NÚMERO MÁXIMO DE COMPARTIMENTOS')
    GARANTIA = models.FloatField(verbose_name='GARANTIA (MESES)')
    REFORCO = models.FloatField(verbose_name='MESES ATÉ O REFORÇO')

    class Meta:
        db_table = 'Serviço'

    def __str__(self):
        return self.DESCRICAO


class Contrato(models.Model):
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='CLIENTE')
    DATAINICIAL = models.DateTimeField(verbose_name='DATA INICIAL')
    DATAFINAL = models.DateTimeField(verbose_name='DATA FINAL')
    VALOR = models.FloatField(verbose_name='VALOR')
    PERIODO = models.IntegerField(verbose_name='PERÍODO')
    ContratoServico = models.ManyToManyField(Servico)

    class Meta:
        db_table = 'Contrato'

    def __str__(self):
        return str(self.ID_CLIENTE)


class HistoricoPadrao(models.Model):
    DESCRICAO = models.CharField(max_length=100, verbose_name='DESCRIÇÃO')

    class Meta:
        db_table = 'Historico_Padrão'

    def __str__(self):
        return self.DESCRICAO


class Contato(models.Model):
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='CLIENTE')
    NOME = models.CharField(max_length=100)
    DEPARTAMENTO = models.CharField(null=True, blank=True, max_length=50)
    TELEFONE = models.ManyToManyField(Telefone)

    class Meta:
        db_table = 'Contato'

    def __str__(self):
        return self.NOME


class FormadePagamento(models.Model):
    DESCRICAO = models.CharField(max_length=100, verbose_name='DESCRIÇÃO')

    class Meta:
        db_table = 'FormaDePagamento'

    def __str__(self):
        return self.DESCRICAO


class Entrada(models.Model):
    DATAHORA = models.DateTimeField(auto_now=True, editable=False)
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.PROTECT, verbose_name='PRODUTO')
    QUANTIDADE = models.FloatField(verbose_name='QUANTIDADE ENTRADA')

    class Meta:
        db_table = 'Entrada'

    def __str__(self):
        return self.ID_PRODUTO


class Tecnico(models.Model):
    ID_FUNCIONARIO = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='NOME DO FUNCIONÁRIO')
    VENCIMENTO_ASO = models.DateField(verbose_name='DATA DE VENCIMENTO DA ASO')
    TecnicoServico = models.ManyToManyField(Servico)

    class Meta:
        db_table = 'Técnico'

    def __str__(self):
        return self.ID_FUNCIONARIO


class OsProposta(models.Model):
    DATAHORACADASTRO = models.DateTimeField(auto_now=True)
    CADASTRADOPOR = models.IntegerField(default=1)
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='CLIENTE')
    TIPOLST = (
        ('P', 'PROPOSTA'),
        ('O', 'ORDEM DE SERVIÇO'),
    )
    TIPO = models.CharField(max_length=1, choices=TIPOLST)
    DATAOS = models.DateField(editable=False, auto_now=True)
    VALORPROPOSTA = models.FloatField(verbose_name='VALOR DA PROPOSTA')
    VALOROS = models.FloatField(verbose_name='VALOR DA ORDEM DE SERVIÇO')
    DATAREFORCO = models.DateField(blank=True, null=True, verbose_name='DATA DO REFORÇO')
    OsPropostaServicos = models.ManyToManyField(Servico)

    class Meta:
        db_table = 'OsProposta'

    def __str__(self):
        return self.TIPO


class Saida(models.Model):
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.PROTECT, verbose_name='PRODUTO')
    QTD = models.FloatField(verbose_name='QUANTIDADE SAÍDA')
    ID_OsProposta = models.ForeignKey(OsProposta, blank=True,
                                      null=True, on_delete=models.PROTECT, verbose_name='ORDEM DE SERVIÇO')
    DATAHORA = models.DateTimeField(auto_now=True)
    OBS = models.CharField(max_length=100)

    class Meta:
        db_table = 'Saída'

    def __str__(self):
        return self.ID_PRODUTO


class EntregaProdutoEquipamento(models.Model):
    ID_TECNICO = models.ForeignKey(Tecnico, on_delete=models.PROTECT, verbose_name='NOME DO TÉCNICO')
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.PROTECT, verbose_name='NOME DO PRODUTO')
    DATAHORA = models.DateTimeField(auto_now=True)
    QTDENTREGUE = models.FloatField(verbose_name='QUANTIDADE ENTREGUE')
    QTDDEVOLVIDA = models.FloatField(verbose_name='QUANTIDADE DEVOLVIDA')
    OBS = models.CharField(max_length=200)

    class Meta:
        db_table = 'EntregaProdutoEquipamento'

    def __str__(self):
        return self.ID_TECNICO


class ServicoProdutoEquipamento(models.Model):
    ID_SERVICO = models.ForeignKey(Servico, on_delete=models.PROTECT, verbose_name='SERVIÇO')
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.PROTECT, verbose_name='NOME DO EQUIPAMENTO/PRODUTO')
    QTD = models.FloatField(null=True, blank=True)
    INSTRUCOES = models.CharField(max_length=200)

    class Meta:
        db_table = 'ServiçoProdutoEquipamento'

    def __str__(self):
        return self.ID_SERVICO


class Caixa(models.Model):
    VALOR = models.FloatField()
    DATAHORA = models.DateTimeField(auto_now=True)
    ID_HISTORICOPADRAO = models.ForeignKey(HistoricoPadrao, on_delete=models.PROTECT, verbose_name='HISTÓRICO PADRÃO')
    COMPLEMENTO = models.CharField(max_length=200)
    ID_OSPROPOSTA = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.PROTECT,
                                      verbose_name='ORDEM DE SERVIÇO')
    ID_CONTA = models.ForeignKey(Conta, on_delete=models.PROTECT, verbose_name='CONTA')
    ID_FORMAPAG = models.ForeignKey(FormadePagamento, on_delete=models.PROTECT)
    ID_LANCADOPOR = models.IntegerField(default=1)

    class Meta:
        db_table = 'Caixa'

    def __str__(self):
        return self.ID_HISTORICOPADRAO


class Mensagem(models.Model):
    TIPOLST = (
        ('Agenda', ''),
        ('Financeiro', ''),
        ('Tecnico', ''),
        ('OS', ''),
    )
    TIPO = models.CharField(choices=TIPOLST, max_length=20, verbose_name='TIPO DE MENSAGEM')
    DATAENVIAR = models.DateTimeField(verbose_name='DATA A SER ENVIADA')
    DATAENVIO = models.DateTimeField(editable=False, blank=True, null=True)
    MEIOLST = (
        ('E-mail', ''),
        ('SMS', ''),
        ('Whatsapp', '')
    )
    MEIO = models.CharField(choices=MEIOLST, max_length=20, verbose_name='MEIO DE ENVIO')
    MENSAGEM = models.TextField()
    ENDERECODESTINATARIO = models.CharField(max_length=100, verbose_name='ENDEREÇO DO DESTINATÁRIO')
    TecnicoMensagem = models.ManyToManyField(Tecnico)
    CaixaMensagem = models.ManyToManyField(Caixa)
    OsMensagem = models.ManyToManyField(OsProposta)

    class Meta:
        db_table = 'Mensagem'

    def __str__(self):
        return self.ENDERECODESTINATARIO


def getultimocliente():
    return Cliente.objects.last()


def filtrocliente(nome, dt1, dt2):
    if nome and dt1 and dt2:
        ano1, mes1, dia1 = dt1.split('-')
        ano2, mes2, dia2 = dt2.split('-')
        dtt1 = date(int(ano1), int(mes1), int(dia1))
        dtt2 = date(int(ano2), int(mes2), int(dia2))
        return Cliente.objects.filter(NOME__icontains=nome, DATAHORACADASTRO__range=(dtt1, dtt2)).order_by('NOME')
    elif dt1 and dt2:
        ano1, mes1, dia1 = dt1.split('-')
        ano2, mes2, dia2 = dt2.split('-')
        dtt1 = date(int(ano1), int(mes1), int(dia1))
        dtt2 = date(int(ano2), int(mes2), int(dia2))
        return Cliente.objects.filter(DATAHORACADASTRO__range=(dtt1, dtt2)).order_by('NOME')
    elif nome:
        return Cliente.objects.filter(NOME__icontains=nome).order_by('NOME')
    else:
        return Cliente.objects.all().order_by('NOME')


def filtrofuncionario(nome, dt1, dt2):
    if nome and dt1 and dt2:
        ano1, mes1, dia1 = dt1.split('-')
        ano2, mes2, dia2 = dt2.split('-')
        dtt1 = date(int(ano1), int(mes1), int(dia1))
        dtt2 = date(int(ano2), int(mes2), int(dia2))
        return Funcionario.objects.filter(NOME__icontains=nome, DATANASCIMENTO__range=(dtt1, dtt2)).order_by('NOME')
    elif dt1 and dt2:
        ano1, mes1, dia1 = dt1.split('-')
        ano2, mes2, dia2 = dt2.split('-')
        dtt1 = date(int(ano1), int(mes1), int(dia1))
        dtt2 = date(int(ano2), int(mes2), int(dia2))
        return Funcionario.objects.filter(DATANASCIMENTO__range=(dtt1, dtt2)).order_by('NOME')
    elif nome:
        return Funcionario.objects.filter(NOME__icontains=nome).order_by('NOME')
    else:
        return Funcionario.objects.select_related().all().order_by('NOME')


def getfonefuncionario():
    return Funcionario.objects.all().order_by('NOME')
