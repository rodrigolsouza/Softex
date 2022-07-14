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
        resultado= print("o segundo número não pode ser igual a zero. Tente novamente")
    return resultado

def calculadora(num1,num2,operador):
    match (operador):
        case '+':
            return soma(num1,num2)
        case'-':
            return subtração(num1,num2)
        case'*':
            return multiplicação(num1,num2)
        case '/':
            return divisão(num1,num2)
        case _:
            return 0

print("Digite dois número e a sinal de operação que deseja efetuar")
num1=int(input("Número 1: "))
num2=int(input("Número 2: "))
operador=input("Operador matemático: ")

resposta=calculadora(num1,num2,operador)
print(resposta)
        
