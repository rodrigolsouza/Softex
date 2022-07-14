'''Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números.
'''


'''
OBS: optei por receber do usuário os números no formato a+bi já que a biblioteca do python já possui uma classe que trabalha com números complexos recebendo o inteiro da parte real e inteiro da parte imaginária.
'''
from TAD_Complexos import *

print("informe os 3 números complexos que deseja manipular escrevendo-os na ordem em que se deseja usá-los para as operações matemáticas. Ex: a+bj onde a e b são números reais ")

#Recebendo as entradas do usuário
entrada1=input("informe o primeiro número complexo: ")
num1Real,num1Imaginario=NumComplexos.tratadorComplexos(entrada1)

entrada2=input("informe o segundo número complexo: ")
num2Real,num2Imaginario=NumComplexos.tratadorComplexos(entrada2)

entrada3=input("informe o terceiro número complexo: ")
num3Real,num3Imaginario=NumComplexos.tratadorComplexos(entrada3)


#Instanciando os objetos
complexo1=NumComplexos(num1Real,num1Imaginario)
complexo2=NumComplexos(num2Real,num2Imaginario)
complexo3=NumComplexos(num3Real,num3Imaginario)        

NumComplexos.imprimirComplexos(complexo1,complexo2,complexo3)

#Efetuando as operações básicas
while True:
    try:
        resultado=None
        NumComplexos.exibir_menu()
        opção=int(input("Digite sua escolha:"))
        if opção==1:
            operacao=NumComplexos.soma(complexo1,complexo2,complexo3)
            resultado=NumComplexos.construtorImaginario(operacao)
        elif opção==2:
            operacao=NumComplexos.subtração(complexo1,complexo2,complexo3)
            resultado=NumComplexos.construtorImaginario(operacao)
        elif opção==3:
            operacao=NumComplexos.multiplicação(complexo1,complexo2,complexo3)
            resultado=NumComplexos.construtorImaginario(operacao)

        elif opção==4:
            operacao=NumComplexos.divisão(complexo1,complexo2,complexo3)
            resultado=NumComplexos.construtorImaginario(operacao)
        elif opção==5:
            print("Obrigado e volta sempre!")
            break
    except:
        print("opção invalida, digite apenas números")
    print("O resultado da operação foi: {}\n" .format(resultado))