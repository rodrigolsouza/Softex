'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''
import datetime

nome=input("Digite seu nome completo: ")
while True:
    try:
        anoNascimento=int(input("Digite o ano de seu nascimento (valores entre 1922 e 2022):"))
        if anoNascimento<1922 or anoNascimento>2021:
            print("opção inválida, digite um ano de nascimento entre 1922 e 2021")
        else:
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            anoAtual= date.strftime("%Y")
            idade=int(anoAtual)-anoNascimento
            print("Olá {}. No ano de {} você completará/completou {} anos " .format(nome, anoAtual,idade))
            break
    except ValueError:
        print("Caracter inválido! Digite apenas números")
