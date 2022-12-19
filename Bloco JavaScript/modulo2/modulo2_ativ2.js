/*
om os conceitos aprendidos, crie um programa de calculadora que: 

receba dois valores, que devem ser salvos em variáveis; 
o usuário deve colocar qual operador ele vai utilizar por meio dos símbolos aritméticos; 
com os dois valores e o operador definido, o programa deve fazer a operação e retornar o resultado; 
se houver divisão, você deve retornar o resultado e a sobra, caso haja alguma. 
*/

var valor1
var valor2
var operador
operador = prompt("Qual operacao deseja efetuar (+) (-) (*) (/)? : \n");
valor1 = parseFloat(prompt("Insira o primeiro numero: \n"));
valor2 = parseFloat(prompt("Insira o segundo numero: \n"));

function CalcOperação(operator, value1, value2) {
    if (operator == "+") {
        console.log('O resultado é', value1 + value2 ) 
    } else if (operator == "-") {
        console.log('O resultado é', value1 - value2 )
    } else if (operator == "*") {
        console.log('O resultado é', value1 * value2 )
    } else if ((operator == "/") && (value2!=0)) {
        result=value1 / value2;
        if (value1 % value2!=0){
            rest=value1 % value2;
            console.log('O resultado é', value1 / value2, 'e o resto é:', value1 % value2 );
        }else{
            console.log('O resultado é', value1 / value2);
        }
    } else {
        throw new Error('Operação inválida');
    }
}