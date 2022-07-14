class NumComplexos():
    def __init__(self,numReal,numImaginario):
        self.parteReal=int(numReal)
        self.parteImaginaria=int(numImaginario)

    @staticmethod
    def imprimirComplexos(complexo1,complexo2,complexo3):
        print("seus números complexos são:\n primeiro número:  Parte Real = {}  e parte imaginária= {}j\n segundo número:  Parte Real = {}  e parte imaginária= {}j\n terceiro número:  Parte Real = {}  e parte imaginária= {}j\n" .format(complexo1.parteReal, complexo1.parteImaginaria, complexo2.parteReal, complexo2.parteImaginaria, complexo3.parteReal, complexo3.parteImaginaria))

    @staticmethod
    def exibir_menu():
            print("\n")
            print("---------MENU-----------")
            menudeopções=["Efetuar soma", "Efetuar subtração", "Efetuar multiplicação","Efetuar divisão", "Sair"]
            for numero,opção in enumerate(menudeopções):
                print(numero+1, "-",opção)
            print("------------------------")


    def construtorImaginario(operação):
        opReal,opImaginaria=operação
        if opImaginaria>=0:
            resultado=str(opReal)+ "+" +str(opImaginaria)+"j"
        else:
            resultado=str(opReal) +str(opImaginaria)+"j"
        return resultado

    @staticmethod
    def soma(num1,num2,num3):
        opReal=num1.parteReal + num2.parteReal+num3.parteReal
        opImaginaria=num1.parteImaginaria + num2.parteImaginaria + num3.parteImaginaria
        return (opReal,opImaginaria)

            
    @staticmethod
    def subtração(num1,num2,num3):
        opReal=num1.parteReal - num2.parteReal-num3.parteImaginaria
        opImaginaria=num1.parteImaginaria - num2.parteImaginaria-num3.parteImaginaria
        
        return (opReal,opImaginaria)


    @staticmethod
    def multiplicaçãoFase1(num1,num2):
        produtoReal=num1.parteReal*num2.parteReal
        produtoImaginario=num1.parteImaginaria*num2.parteImaginaria*(-1)
        produtoRealImag=(num1.parteReal*num2.parteImaginaria) + (num1.parteImaginaria*num2.parteReal)
        resParteReal=produtoReal+produtoImaginario
        return(resParteReal,produtoRealImag)

    @staticmethod
    def multiplicaçãoFase2(multi1,num3):
        resParteReal,produtoRealImag=multi1
        produtoReal2=num3.parteReal*resParteReal
        produtoImaginario2=num3.parteImaginaria*produtoRealImag*(-1)
        produtoRealImag2=num3.parteReal*produtoRealImag + num3.parteImaginaria*resParteReal

        opReal=produtoReal2+produtoImaginario2
        opImaginaria=produtoRealImag2
        return(opReal,opImaginaria)

    @staticmethod
    def multiplicação(num1,num2,num3):
        opReal,opImaginaria=NumComplexos.multiplicaçãoFase2(NumComplexos.multiplicaçãoFase1(num1,num2),num3)
        return(opReal,opImaginaria)

    @staticmethod
    def divisão(num1,num2,num3):
        condição=False
        conjugadoReal=num2.parteReal
        conjugadoImaginario=-num2.parteImaginaria
        numConjugado=NumComplexos(conjugadoReal,conjugadoImaginario)
        realNumerador,imaginarioNumerador=NumComplexos.multiplicaçãoFase1(num1,numConjugado)
        produtoDenominador1, produtoDenominador2=NumComplexos.multiplicaçãoFase1(num2,numConjugado)
        denominador=produtoDenominador1 + produtoDenominador2

        resultadoReal=int(realNumerador)/denominador
        resultadoImaginario=int(imaginarioNumerador)/denominador

        objeto=NumComplexos(resultadoReal,resultadoImaginario)
        if condição=="False":
            condição=True
            objetoFinal=NumComplexos.divisão(objeto,num3)
            opReal=objetoFinal.parteReal
            opImaginaria=objetoFinal.parteImaginaria
        else:
            opReal=resultadoReal
            opImaginaria=resultadoImaginario
        return (opReal,opImaginaria)
        

    @staticmethod
    def tratadorComplexos(num):
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
