'''Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.'''

def soma(num1,num2):
    return num1+num2

def subtração(num1,num2):
    return num1-num2

def multiplicação(num1,num2):
    return num1*num2

def divisão(num1,num2):
    resultado=None
    if num2!=0:
        resultado= num1/num2
    else:
        resultado= print("o segundo número não pode ser igual a zero")
    return resultado

def calculadora(num1,num2,operador):
    switch(operador) {
        "+":soma(num1,num2)
    }
