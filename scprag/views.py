from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from scprag.models import Cliente
from scprag.models import Local
from scprag.models import Contato
from scprag.models import Funcionario
from scprag.models import filtrocliente
from scprag.models import filtrofuncionario
#from scprag.models import getfonefuncionario
from scprag.models import Telefone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


@login_required(login_url='/loginscprag/')
def alertas(request):
    return render(request, 'alertas.html')


def index(request):
    return redirect('/alertas/')


def loginscprag(request):
    return render(request, 'loginscprag.html')


def autentica_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return redirect('/')


def logoutscprag(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/loginscprag/')
def listaCliente(request):
    nome = request.GET.get('nome')
    dt1 = request.GET.get('dt1')
    dt2 = request.GET.get('dt2')
 #   if nome:
 #       cliente = Cliente.objects.filter(NOME__icontains=nome)
    cliente = filtrocliente(nome,dt1,dt2)
    dados = {'clientes': cliente}
    return render(request, 'cliente.html', dados)


@login_required(login_url='/loginscprag/')
def cadastrar_cliente(request):
    id_cliente = request.GET.get('id')
    id_local = request.GET.get('idlocal')
    id_contato = request.GET.get('idcontato')
    dados = {}
    if id_cliente:
        dados['cliente'] = Cliente.objects.get(id=id_cliente)
        if id_local:
            dados['cliente'].setLocal(id_local)
        if id_contato:
            dados['cliente'].setContato(id_contato)
        dados['cliente'].setSalvarCliente('salvo')
    return render(request, 'cadastrar_cliente.html', dados)


@login_required(login_url='/loginscprag/')
def submit_cliente(request):
    if request.POST:
        btn1 = request.POST.get('_save')
        btn2 = request.POST.get('_addanother')
        btn1local = request.POST.get('_savelocal')
        btn2local = request.POST.get('_addanotherlocal')
        btn1contato = request.POST.get('_savecontato')
        btn2contato = request.POST.get('_addanothercontato')
        id_cliente = request.POST.get('id_cliente')
        id_local = request.POST.get('id_clientelocal')
        id_contato = request.POST.get('id_clientecontato')
        if btn1contato or btn2contato:
            nome=request.POST.get('NOMECONTATO')
            departamento=request.POST.get('DEPARTAMENTO')
            telefones = request.POST.get('telefonesC').split('\r\n')
            if id_contato and id_contato != '0':
                contato = Contato.objects.get(id=id_contato)
                contato.NOME = nome.upper()
                contato.DEPARTAMENTO = departamento.upper()
                contato.save()
                Telefone.objects.filter(contato=id_contato).delete()
            else:
                cliente = Cliente.objects.get(id=id_cliente)
                Contato.objects.create(NOME=nome.upper(),
                                       DEPARTAMENTO=departamento.upper(),
                                       ID_CLIENTE=cliente)
                contato = Contato.objects.last()
                id_contato = str(contato.id)
            for telefone in telefones:
                t = Telefone(TELEFONE=telefone.strip(' '))
                if (len(t.TELEFONE.strip()) > 3):
                    t.save()
                    contato.TELEFONE.add(t)
            if btn1contato == 'Salvar':
                return redirect('/cadastrar_cliente/?id='+id_cliente+'&idcontato='+id_contato)
            elif btn2contato == 'Salvar e adicionar outro(a)':
                return redirect('/cadastrar_cliente/?id='+id_cliente+'&idcontato=0')
        elif btn1local or btn2local:
            cep=request.POST.get('CEP')
            logradouro=request.POST.get('LOGRADOURO')
            numero=request.POST.get('NUMERO')
            referencia=request.POST.get('REFERENCIA')
            coordenadas=request.POST.get('COORDENADAS')
            area=request.POST.get('AREA')
            compartimentos=request.POST.get('COMPARTIMENTOS')
            banheiros=request.POST.get('BANHEIROS')
            obs=request.POST.get('OBS')
            if id_local and id_local != '0':
                local = Local.objects.get(id=id_local)
                local.CEP = cep
                local.LOGRADOURO = logradouro.upper()
                local.NUMERO = numero
                local.REFERENCIA = referencia.upper()
                local.COORDENADAS = coordenadas
                local.AREA = area
                local.COMPARTIMENTOS = compartimentos
                local.BANHEIROS = banheiros
                local.OBS = obs.upper()
                local.save()
            else:
                cliente = Cliente.objects.get(id=id_cliente)
                Local.objects.create(CEP=cep,
                                   LOGRADOURO=logradouro.upper(),
                                   NUMERO=numero,
                                   REFERENCIA=referencia.upper(),
                                   COORDENADAS=coordenadas,
                                   AREA=area,
                                   COMPARTIMENTOS=compartimentos,
                                   BANHEIROS=banheiros,
                                   ID_CLIENTE=cliente,
                                   OBS=obs.upper())
                local = Local.objects.last()
                id_local = str(local.id)
            if btn1local == 'Salvar':
                return redirect('/cadastrar_cliente/?id='+id_cliente+'&idlocal='+id_local)
            elif btn2local == 'Salvar e adicionar outro(a)':
                return redirect('/cadastrar_cliente/?id='+id_cliente+'&idlocal=0')
        else:
            nome = request.POST.get('NOME')
            pfpj = request.POST.get('PFPJ')
            cpfcnpj = request.POST.get('CPFCNPJ')
            email1 = request.POST.get('EMAIL1')
            email2 = request.POST.get('EMAIL2')
            telefones = request.POST.get('telefones').split('\r\n')
        if id_cliente:
            cliente = Cliente.objects.get(id=id_cliente)
            cliente.NOME = nome.upper()
            cliente.PFPJ = pfpj
            cliente.CPFCNPJ = cpfcnpj
            cliente.EMAIL1 = email1
            cliente.EMAIL2 = email2
            cliente.save()
            cliente.setSalvarCliente('salvo')
            Telefone.objects.filter(cliente=id_cliente).delete()
        else:
            Cliente.objects.create(NOME=nome.upper(),
                               PFPJ=pfpj,
                               CPFCNPJ=cpfcnpj,
                               EMAIL1=email1,
                               EMAIL2=email2)
            cliente = Cliente.objects.last()
            cliente.setSalvarCliente('salvo')
        for telefone in telefones:
            t = Telefone(TELEFONE=telefone.strip(' '))
            if (len(t.TELEFONE.strip()) > 3):
                t.save()
                cliente.TELEFONE.add(t)
        if btn1 == 'Salvar e retornar para listagem':
            return redirect('/clientes/')
        elif btn2 == 'Salvar e adicionar outro(a)':
            return render(request, 'cadastrar_cliente.html')
        else:
            dados = {}
            dados['cliente'] = Cliente.objects.get(id=cliente.id)
            dados['cliente'].setSalvarCliente('salvo')
            return redirect('/cadastrar_cliente/?id=' + str(cliente.id) + '&idlocal=0')
            # return render(request, 'cadastrar_cliente.html', dados)


@login_required(login_url='/loginscprag/')
def delete_cliente(request, id_cliente):
    Cliente.objects.filter(id=id_cliente).delete()
    return redirect('/clientes/')


@login_required(login_url='/loginscprag/')
def delete_local(request, id_cliente, id_local):
    Local.objects.filter(id=id_local).delete()
    return redirect('/cadastrar_cliente/?id='+str(id_cliente)+'&idlocal=0')


@login_required(login_url='/loginscprag/')
def delete_contato(request, id_cliente, id_contato):
    Contato.objects.filter(id=id_contato).delete()
    return redirect('/cadastrar_cliente/?id='+str(id_cliente)+'&idcontato=0')


@login_required(login_url='/loginscprag/')
def listaFuncionario(request):
    nome = request.GET.get('nome')
    dt1 = request.GET.get('dt1')
    dt2 = request.GET.get('dt2')
 #   if nome:
 #       cliente = Cliente.objects.filter(NOME__icontains=nome)
 #   for f in getfonefuncionario():
 #       print(f)
    funcionario = filtrofuncionario(nome,dt1,dt2)

    dados = {'funcionarios': funcionario}
    return render(request, 'funcionario.html', dados)


@login_required(login_url='/loginscprag/')
def cadastrar_funcionario(request):
    id_funcionario = request.GET.get('id')
    dados = {}
    if id_funcionario:
        dados['funcionario'] = Funcionario.objects.get(id=id_funcionario)
    return render(request, 'cadastrar_funcionario.html', dados)


@login_required(login_url='/loginscprag/')
def submit_funcionario(request):
    if request.POST:
        btn1 = request.POST.get('_save')
        btn2 = request.POST.get('_addanother')
        id_funcionario = request.POST.get('id_funcionario')
        nome = request.POST.get('NOME')
        email = request.POST.get('EMAIL')
        data_nascimento = request.POST.get('DATA_NASCIMENTO')
        telefones = request.POST.get('telefones').split('\r\n')

        if id_funcionario:
            funcionario = Funcionario.objects.get(id=id_funcionario)
            funcionario.NOME = nome
            funcionario.EMAIL = email
            funcionario.DATA_NASCIMENTO = data_nascimento
            funcionario.save()
            Telefone.objects.filter(funcionario=id_funcionario).delete()

            # Cliente.objects.filter(id=id_cliente).update(
            #    NOME=nome,
            #    PFPJ=pfpj,
            #    CPFCNPJ=cpfcnpj,
            #    EMAIL1=email1,
            #    EMAIL2=email2)
        else:
            Funcionario.objects.create(NOME=nome,
                               EMAIL=email,
                               DATA_NASCIMENTO=data_nascimento)
            funcionario = Funcionario.objects.last()
        for telefone in telefones:
            t = Telefone(TELEFONE=telefone)
            if (len(t.TELEFONE.strip())>3 ):
                t.save()
                funcionario.TELEFONE.add(t)

        if btn1 == 'Salvar':
            return redirect('/funcionarios/')
        elif btn2 == 'Salvar e adicionar outro(a)':
            return render(request, 'cadastrar_funcionario.html')
        else:
            dados = {}
            dados['funcionario'] = Funcionario.objects.get(id=funcionario.id)
            return render(request, 'cadastrar_funcionario.html', dados)

@login_required(login_url='/loginscprag/')
def delete_funcionario(request, id_funcionario):
    Funcionario.objects.filter(id=id_funcionario).delete()
    return redirect('/funcionarios/')
