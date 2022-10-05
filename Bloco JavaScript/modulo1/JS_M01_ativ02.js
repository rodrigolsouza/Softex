/*
Acesse pelo menos dois sites de sua preferência e os inspecione com o botão direito do mouse na página web.
Com o código fonte aberto você deve: 

Verificar no código algum elemento que utilize JavaScript; 
Marcar alguns elementos do site; 
Explicar como ele se comporta. Exemplo: entrar no site do Google, inspecionar o botão de pesquisa, verificar o código e explicar qual a finalidade do botão. 

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo. 
*/

/*********************************************RESPOSTA:*********************************************************

LINK 1: Na página https://www.sismepe.pe.gov.br:4443/login.php escolhi o elemento <div>  que possui o atributo class= "menu" dentro dela há uma tag <script> que é do tipo text/javascript ( type passado como atributo). Na tela essa tag consiste num botão chamdo MEU SISMEPE que ao ser clicado ativa o script que executa os seguintes comandos:
 1-Um comando de criação de objeto XMLHTTPRequest

2- Uma função logar que pega os dados de login e de senha do usuário e chama a função abrirpag()

 3-Uma função(chamada abrirPag) que recebe os valores de login e senha como parâmetros e envia via método post para o servidor para fazer validação no banco de dados o usuário 

4- Uma função (chamada mudançaLogin) que carrega a página com os dados do usuário passados na função anterior ou informar que houve erro no login ou o usuário não existe( de acordo com a resposta enviada do servidor)
*/

/*LINK 2: No link https://www.unimedrecife.com.br/# nela existe a função:
<script type="text/javascript">
function abrir(texto) {
			$("#exibe").html('');
			$("#exibe").append(texto);
			$("#popup").fadeIn(); // ou slideDown()
		}

function fechar(texto) {
			$("#popup").append(texto).fadeOut(); // ou slideUp()
		}
</script>
que ao que entendi ela parece ser uma função que exibe o popup sobre boleto digital que a página exibe quando a pessoa entra no site ou atualiza a página.
*/
