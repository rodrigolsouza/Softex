/*Escolha algum código executável em JavaScript feito em atividades passadas e o coloque no Node.js. Para isso, você deve ter o Node.js instalado. Após fazer essa migração, coloque seu código no arquivo "index.js", teste e tire um print.*/

const promptSync = require('prompt-sync')({sigint: true});

var somaNotas=0;
var Nota1 = parseFloat(promptSync("Qual é a sua primeira nota?"))
    somaNotas+=Nota1;
var Nota2 = parseFloat(promptSync("Qual a sua segunda nota?"))
    somaNotas+=Nota2;
var Nota3 = parseFloat(promptSync("Qual a sua terceira nota?"))
    somaNotas+=Nota3;

var resultado=(somaNotas/3>=7)?'Aprovado': 'Reprovado';
console.log(resultado)