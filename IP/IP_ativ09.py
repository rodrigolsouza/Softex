'''
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

'''

def exibir_menu():
    print("\n")
    print("---------MENU-----------")
    menudeopções=[ "Sair","Efetuar soma", "Efetuar subtração", "Efetuar multiplicação","Efetuar divisão"]
    for numero,opção in enumerate(menudeopções):
        print(numero, "-",opção)
    print("------------------------")

def definir_valores():
    valor1=int(input("digite o primeiro número: "))
    valor2=int(input("digite o segundo número: "))
    return valor1,valor2

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
        resultado= print("\nO segundo número não pode ser igual a zero.Tente novamente")
    return resultado

while True:
    try:
        resultado=None
        exibir_menu()
        opção=int(input("Digite sua escolha: "))
        if opção==0:
            break
        elif opção==1:
            num1,num2=definir_valores()
            resultado=soma(num1,num2)
        elif opção==2:
            num1,num2=definir_valores()
            resultado=subtração(num1,num2)
        elif opção==3:
            num1,num2=definir_valores()
            resultado=multiplicação(num1,num2)

        elif opção==4:
            num1,num2=definir_valores()
            resultado=divisão(num1,num2)
        else:
            resultado="Essa opção não existe"
    except:
        resultado="opção inválida, digite apenas números"
    print("\n")
    print("O resultado da operação foi: {}\n" .format(resultado))