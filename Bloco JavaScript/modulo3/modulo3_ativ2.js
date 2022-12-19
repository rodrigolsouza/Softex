/*Crie um programa que contenha os seguintes tipos de funções:

1. uma função tradicional com a palavra reservada “Function” e sem nenhum parâmetro;
2. uma função tradicional com parâmetros e um retorno de valor;
3. uma arrow function com parâmetros e que retorne um valor.

Crie um programa que utilize essas três funções de forma lógica, por exemplo: um programa de calculadora.*/

/* FUNÇÃO TRADICIONAL*/
function congratulacao(){
    console.log("Hello!");
};

console.log(congratulacao);

/*FUNÇÃO TRADICIONAL COM RETORNO E COM PARÂMETROS*/

let anonima=function(name){
    return "Welcome" + name;
};

console.log(anonima("Rodrigo"));

/*FUNÇÃO COM PARÂMETROS E QUE RETORNE UM VALOR*/
function exibirOperacoes(n,f){
    for(let i=0; i<n; i++){
        f(i);
    };
};

repeat(10,x=>{let p= Math.pow(x,2);
    console.log(`O quadrado de ${x} é ${p}`);
});