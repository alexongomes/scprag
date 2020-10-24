/*
    Captura parâmetros de URL com JS
    Créditos: http://profanderson.blog.etecarmine.com.br/
*/
function SalvaCli() {
    document.getElementById('salvarcliente').value = 'salvar';
    }


function confirma(msg, url) {
    var result = confirm(msg);
    if (result) {
        window.open(url, "_self");
    }
}

function getidlocalidcontato() {
    if (document.getElementById('url').innerHTML.indexOf('idlocal') >= 0)
    {
        var posicaoigual = document.getElementById('url').innerHTML.indexOf('=', document.getElementById('url').innerHTML.indexOf('idlocal'));
        var posicaofinal = document.getElementById('url').innerHTML.length;
        document.getElementById('id_clientelocal').value = (document.getElementById('url').innerHTML.substring(parseInt(posicaoigual)+1, parseInt(posicaofinal))).trim();
        document.getElementById('Locais').value = document.getElementById('id_clientelocal').value;
        trocaaba('a2');
    }
    else if (document.getElementById('url').innerHTML.indexOf('idcontato') >= 0)
    {
        var posicaoigual = document.getElementById('url').innerHTML.indexOf('=', document.getElementById('url').innerHTML.indexOf('idcontato'));
        var posicaofinal = document.getElementById('url').innerHTML.length;
        document.getElementById('id_clientecontato').value = (document.getElementById('url').innerHTML.substring(parseInt(posicaoigual)+1, parseInt(posicaofinal))).trim();
        document.getElementById('Contatos').value = document.getElementById('id_clientecontato').value;
        trocaaba('a3');
    }
//    document.getElementById('id_clientelocal').value = document.getElementById('url').innerHTML.indexOf.substring((document.getElementById('url').innerHTML.indexOf('=', (document.getElementById('url').innerHTML.indexOf('idlocal')))), document.getElementById('url').innerHTML.indexOf('/', (document.getElementById('url').innerHTML.indexOf('idlocal'))))
//    alert(document.getElementById('url').innerHTML.indexOf('/', (document.getElementById('url').innerHTML.indexOf('idlocal'))))
}

function abreAba() {
    //captura a url da página
    var url = window.location.href;
    //tenta localizar o ?
    var res = url.split('?');
    if (res[1] === undefined) {
    }
    if (res[1] !== undefined) {
        //tenta localizar os & (pode haver mais de 1)
        var parametros = res[1].split('&');
        //qtd. de parâmetros que serão tratados pelo laço.
        var qtdParametrosParaLer = 5;
        //guarda o nome dos parâmetros e os valores e, vetores.
        var parametroEncontrado = new Array();
        var valorParametro = new Array();
        for (var cont = 0; cont<=qtdParametrosParaLer; cont++)
        {
            if (parametros[cont] !== undefined)
            {
                captura = parametros[cont].split('=');
                parametroEncontrado[cont] = captura[0];
                valorParametro[cont] = captura[1];
                if (valorParametro[cont] !== '')
                {
                    if (parametroEncontrado[cont] == 'idclientelocal')
                    {
                        document.getElementById('id_clientelocal') = valorParametro[cont];
                        trocaaba('a2')
                    }
                    else if (parametroEncontrado[cont] == 'idclientecontato')
                    {
                        document.getElementById('id_clientecontato') = valorParametro[cont];
                        trocaaba('a3')
                    }
                }
            }
        }
    }
}

function CapturaParametrosUrl() {
    //captura a url da página
    var url = window.location.href;
    //tenta localizar o ?
    var res = url.split('?');
    if (res[1] === undefined) {
    }
    if (res[1] !== undefined) {
        //tenta localizar os & (pode haver mais de 1)
        var parametros = res[1].split('&');
        //qtd. de parâmetros que serão tratados pelo laço.
        var qtdParametrosParaLer = 5;
        //guarda o nome dos parâmetros e os valores e, vetores.
        var parametroEncontrado = new Array();
        var valorParametro = new Array();
        for (var cont = 0; cont<=qtdParametrosParaLer; cont++)
        {
            if (parametros[cont] !== undefined)
            {
                captura = parametros[cont].split('=');
                parametroEncontrado[cont] = captura[0];
                valorParametro[cont] = captura[1];
                if (valorParametro[cont] !== '')
                {
                    document.getElementById('resultado').innerHTML += parametroEncontrado[cont] + '=' + valorParametro[cont] + '  +   ';
                }
            }
        }
    }
}
function addopt(cxfone, impfone){
    var valoradd = document.getElementById(impfone).value;
    var Telefones = document.getElementById(cxfone);
    var adcionar = false;
    if (Telefones.value.indexOf(valoradd) == -1){adcionar=true}
    if (adcionar==true){
        Telefones.value = valoradd.trim() + "\n" + Telefones.value.trim();
        document.getElementById(impfone).value = "";
    }
}
function trocaaba(aba)
{
    if (document.getElementById('a1').style.display == "block") {
      if  (document.getElementById('salvarcliente').value == 'salvar'){
            alert('Salve os dados básicos antes de mudar de guia.');
            return;
        }
    }
    if (aba == 'a1')
    {
    /* Habilitar controles da Aba a1 */
        document.getElementById('a1').style.display = "block";
        document.getElementById('aba1').classList.remove("btnnormal");
        document.getElementById('aba1').classList.add("btnpressionado");
        document.getElementById("lblnome").classList.add("required");
        document.getElementById("NOME").required = true;
    /* Desabilitar controles da Aba a2 */
        document.getElementById("lbllogradouro").classList.remove("required");
        document.getElementById("lblnumero").classList.remove("required");
        document.getElementById("lblcompartimentos").classList.remove("required");
        document.getElementById("lblcep").classList.remove("required");
        document.getElementById("LOGRADOURO").removeAttribute("required");
        document.getElementById("NUMERO").removeAttribute("required");
        document.getElementById("COMPARTIMENTOS").removeAttribute("required");
        document.getElementById("CEP").removeAttribute("required");
        document.getElementById('a2').style.display = "none";
        document.getElementById('aba2').classList.remove("btnpressionado");
        document.getElementById('aba2').classList.add("btnnormal");
    /* Desabilitar controles da aba a3 */
        document.getElementById('aba3').classList.remove("btnpressionado");
        document.getElementById('aba3').classList.add("btnnormal");
        document.getElementById("NOMECONTATO").removeAttribute("required");
        document.getElementById("lblnomecontato").classList.remove("required");
    }
    else if(aba == 'a2')
    {
    /* Desabilitar controles da Aba 1 */
        document.getElementById('a1').style.display = "none";
        document.getElementById('aba1').classList.add("btnnormal");
        document.getElementById('aba1').classList.remove("btnpressionado");
        document.getElementById("lblnome").classList.remove("required");
        document.getElementById("NOME").removeAttribute("required");
    /* Habilitar controles da aba 2 */
        document.getElementById("lbllogradouro").classList.add("required");
        document.getElementById("lblnumero").classList.add("required");
        document.getElementById("lblcompartimentos").classList.add("required");
        document.getElementById("LOGRADOURO").required = true;
        document.getElementById("NUMERO").required = true;
        document.getElementById("COMPARTIMENTOS").required = true;
        document.getElementById("lblcep").classList.add("required");
        document.getElementById("CEP").required = true;
        document.getElementById('a2').style.display = "block";
        document.getElementById('aba2').classList.remove("btnnormal");
        document.getElementById('aba2').classList.add("btnpressionado");
    /* desabilitar controles da aba 3 */
        document.getElementById('a3').style.display = "none";
        document.getElementById('aba3').classList.remove("btnpressionado");
        document.getElementById('aba3').classList.add("btnnormal");
        document.getElementById("NOMECONTATO").removeAttribute("required");
        document.getElementById("lblnomecontato").classList.remove("required");
    }
    else
    {
    /* Desabilitar controles da aba 1 */
        document.getElementById('a1').style.display = "none";
        document.getElementById('aba1').classList.remove("btnpressionado");
        document.getElementById('aba1').classList.add("btnnormal");
        document.getElementById("lblnome").classList.remove("required");
        document.getElementById("NOME").removeAttribute("required");
   /* Desabilitar controles da aba 2 */
        document.getElementById("lbllogradouro").classList.remove("required");
        document.getElementById("lblnumero").classList.remove("required");
        document.getElementById("lblcompartimentos").classList.remove("required");
        document.getElementById("lblcep").classList.remove("required");
        document.getElementById("LOGRADOURO").removeAttribute("required");
        document.getElementById("NUMERO").removeAttribute("required");
        document.getElementById("COMPARTIMENTOS").removeAttribute("required");
        document.getElementById("CEP").removeAttribute("required");
        document.getElementById('a2').style.display = "none";
        document.getElementById('aba2').classList.remove("btnpressionado");
        document.getElementById('aba2').classList.add("btnnormal");
   /* habilitar controles da aba 3   */
        document.getElementById('a3').style.display = "block";
        document.getElementById('aba3').classList.add("btnpressionado");
        document.getElementById('aba3').classList.remove("btnnormal");
        document.getElementById("lblnomecontato").classList.add("required");
        document.getElementById("NOMECONTATO").required = true;
    }
}
/* PESQUISAR O ENDEREÇO PELO CEP ****************************/
    function limpa_formulário_cep() {
            //Limpa valores do formulário de cep.
            /*
            document.getElementById('rua').value=("");
            document.getElementById('bairro').value=("");
            document.getElementById('cidade').value=("");
            document.getElementById('uf').value=("");
            document.getElementById('ibge').value=(""); */
    }

    function meu_callback(conteudo) {
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('rua').value=(conteudo.logradouro);
            document.getElementById('bairro').value=(conteudo.bairro);
            document.getElementById('cidade').value=(conteudo.localidade);
            document.getElementById('uf').value=(conteudo.uf);
            document.getElementById('ibge').value=(conteudo.ibge);
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
        }
    }

    function pesquisacep(valor) {

        //Nova variável "cep" somente com dígitos.
        var cep = valor.replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                document.getElementById('rua').value="...";
                document.getElementById('bairro').value="...";
                document.getElementById('cidade').value="...";
                document.getElementById('uf').value="...";
                document.getElementById('ibge').value="...";

                //Cria um elemento javascript.
                var script = document.createElement('script');

                //Sincroniza com o callback.
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

                //Insere script no documento e carrega o conteúdo.
                document.body.appendChild(script);

            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    };
