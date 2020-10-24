from django.contrib import admin
from scprag.models import *

# Register your models here.

class Clienteadmin(admin.ModelAdmin):
    list_display = ('NOME', 'CPFCNPJ', 'EMAIL1', 'EMAIL2')

class Contratoadmin(admin.ModelAdmin):
    list_display = ('ID_CLIENTE', 'DATAINICIAL', 'DATAFINAL')

class OsPropostaAdmin(admin.ModelAdmin):
    list_display = ('ID_CLIENTE', 'TIPO', 'DATAHORACADASTRO')


class Funcionarioadmin(admin.ModelAdmin):
    list_display = ('NOME', 'EMAIL', 'DATA_NASCIMENTO')


admin.site.register(Cliente, Clienteadmin)
admin.site.register(Contrato, Contratoadmin)
admin.site.register(Conta)
admin.site.register(EntregaProdutoEquipamento)
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(OsProposta, OsPropostaAdmin)
admin.site.register(ServicoProdutoEquipamento)
admin.site.register(Local)
admin.site.register(Servico)
admin.site.register(Caixa)
admin.site.register(FormadePagamento)
admin.site.register(HistoricoPadrao)
admin.site.register(Tecnico)
admin.site.register(Funcionario, Funcionarioadmin)
admin.site.register(Telefone)
admin.site.register(Mensagem)
admin.site.register(Produto)
admin.site.register(Contato)
