class NumComplexos():
    def __init__(self,numReal,numImaginario):
        self.parteReal=int(numReal)
        self.parteImaginaria=int(numImaginario)

    @staticmethod
    def exibir_menu():
            print("\n")
            print("---------MENU-----------")
            menudeopções=["Efetuar soma", "Efetuar subtração", "Efetuar multiplicação","Efetuar divisão", "Sair"]
            for numero,opção in enumerate(menudeopções):
                print(numero+1, "-",opção)
            print("------------------------")


    def soma(num1,num2):
        somaReal=num1.parteReal + num2.parteReal
        somaImaginaria=num1.parteImaginaria + num2.parteImaginaria
        if somaImaginaria>=0:
            resultado=str(somaReal)+ "+" +str(somaImaginaria)+"j"
        else:
            resultado=str(somaReal) +str(somaImaginaria)+"j"
            
        return resultado

    def subtração(num1,num2):
        subtraçãoReal=num1.parteReal - num2.parteReal
        subtraçãoImaginaria=num1.parteImaginaria - num2.parteImaginaria
        if subtraçãoImaginaria>=0:
            resultado=str(subtraçãoReal)+ "+" +str(subtraçãoImaginaria)+"j"
        else:
            resultado=str(subtraçãoReal) +str(subtraçãoImaginaria)+"j"
        
        return resultado

    def multiplicação(num1,num2):
        produtoReal=num1.parteReal*num2.parteReal
        produtoImaginario=num1.parteImaginaria*num2.parteImaginaria
        produtoRealImag=(num1.parteReal*num2.parteImaginaria) + (num1.parteImaginaria*num2.parteReal)
        if produtoRealImag>=0:
            resultado=str(produtoReal+ produtoImaginario*(-1))+ "+" +str(produtoRealImag) +"j"  
        else:
            resultado=str(produtoReal+ produtoImaginario*(-1)) +str(produtoRealImag) +"j"
        
        return resultado

    def teste(num1,num2):
        print(num1.parteReal)

    def divisão(num1,num2):
        conjugadoReal=num2.parteReal
        conjugadoImaginario=-num2.parteImaginaria
        numConjugado=NumComplexos(conjugadoReal,conjugadoImaginario)
        produtoNumerador=NumComplexos.multiplicação(num1,numConjugado)
        produtoDenominador=NumComplexos.multiplicação(num2,numConjugado)
        produtoDenominador1, produtoDenominador2=tratador_entrada(produtoDenominador)
        denominador=int(produtoDenominador1)+ int(produtoDenominador2)
        realNumerador,imaginarioNumerador=tratador_entrada(produtoNumerador)
        resultadoReal=int(realNumerador)/denominador
        resultadoImaginario=int(imaginarioNumerador)/denominador
        if resultadoImaginario>=0:
            resultado=str(resultadoReal)+ "+" +str(resultadoImaginario)+"j"
        else:
            resultado=str(resultadoReal) +str(resultadoImaginario)+"j"
        return resultado
        

def tratador_entrada(num):
    real=""
    imaginario=""
    for x in num:
        if x=="+" or x=="-":
            if real=="":
                real+=str(x)
            else:
                imaginario+=str(x)
        elif x!="+" and x!="-":
            if imaginario=="":
                real+=str(x)
            else:
                imaginario+=str(x)
    imaginario=imaginario[:-1]
    return(real,imaginario)