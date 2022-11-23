'''Estruture três códigos, os quais devem conter uma função de manipulação de 
string que obtenha resultado.'''

'''OBS: tirar as aspas para rodar o código'''

'''
CODIGO 1:
'''
'''
texto=" ado ado cada um no seu quadrado"
posicao=0
ultimaposicao=0
contstring=0
while posicao!=-1:
    posicao=texto.find("ado",ultimaposicao)
    if posicao!=-1:
        contstring+=1
    ultimaposicao+=posicao
print(contstring)
'''

'''
CODIGO 2:
'''
'''
nome="rodrigo lopes de souza"
numero_de_o=nome.count("o")
print(numero_de_o)

'''

'''
CODIGO 3:
'''

'''
nome="tchaicóvsky"
print(nome.capitalize())
'''