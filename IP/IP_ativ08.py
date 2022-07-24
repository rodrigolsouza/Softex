'''Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.'''

def exibir_menu():
    print("\n")
    print("---------MENU-----------")
    menudeopções=["Efetuar soma", "Efetuar subtração", "Efetuar multiplicação","Efetuar divisão"]
    for numero,opção in enumerate(menudeopções):
        print(numero+1, "-",opção)
    print("------------------------")

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

def calculadora(num1,num2,opção):
    match (opção):
        case 1:
            return soma(num1,num2)
        case 2:
            return subtração(num1,num2)
        case 3:
            return multiplicação(num1,num2)
        case 4:
            return divisão(num1,num2)
        case _:
            return 0

print("Digite dois número")
num1=int(input("Número 1: "))
num2=int(input("Número 2: "))
exibir_menu()
opção=int(input("digite a operação desejada: "))
resposta=calculadora(num1,num2,opção)
print(resposta)
        
