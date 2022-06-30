'''Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
O método deve:

- calcular três números complexos;
- realizar todas as operações básicas;
- e imprimir as propriedades real e img do números.'''

from TAD_Complexos import *

print("informe os 3 números complexos que deseja manipular escrevendo-os na ordem em que se deseja usá-los para as operações matemáticas. Ex: a+bj onde a e b são números reais ")

entrada1=input("informe o primeiro número complexo: ")
num1Real,num1Imaginario=tratador_entrada(entrada1)
complexo1=NumComplexos(num1Real,num1Imaginario)

entrada2=input("informe o segundo número complexo: ")
num2Real,num2Imaginario=tratador_entrada(entrada2)
complexo2=NumComplexos(num2Real,num2Imaginario)

entrada3=input("informe o terceiro número complexo: ")
num3Real,num3Imaginario=tratador_entrada(entrada3)
complexo3=NumComplexos(num3Real,num3Imaginario)        

print("seus números complexos são:\n primeiro número:  Parte Real = {}  e parte imaginária= {}j\n segundo número:  Parte Real = {}  e parte imaginária= {}j\n terceiro número:  Parte Real = {}  e parte imaginária= {}j\n" .format(complexo1.parteReal, complexo2.parteImaginaria, complexo2.parteReal, complexo2.parteImaginaria, complexo3.parteReal, complexo3.parteImaginaria))

while True:
    try:
        resultado=None
        NumComplexos.exibir_menu()
        opção=int(input("Digite sua escolha:"))
        if opção==1:
            resultado=NumComplexos.soma(complexo1,complexo2)
        elif opção==2:
            resultado=NumComplexos.subtração(complexo1,complexo2)
        elif opção==3:
            resultado=NumComplexos.multiplicação(complexo1,complexo2)
        elif opção==4:
            resultado=NumComplexos.divisão(complexo1,complexo2)
        elif opção==5:
            print("Obrigado e volta sempre!")
            break
    except:
        print("opção invalida, digite apenas números")
    print("O resultado da operação foi: {}\n" .format(resultado))