'''
Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0

O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve retornar uma mensagem para votar novamente.

Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a quantidade de votos de cada candidato, os brancos e nulos 
'''
def exibir_menu():
            print("\n")
            print("---------Candidatos-----------")
            print(" - candidato_X => 889\n - candidato_Y => 847\n - candidato_Z => 515\n - branco => 0\n")
            print("------------------------")

def apontar_vencendor(x,y,z,branco,nulo):
    vencedor=None
    if x>y and x>z and x>branco and x>nulo:
        vencedor="Candidato_X"
    elif y>z and y>branco and y>nulo:
        vencedor="Candidato_Y"
    elif z>branco and z>nulo:
        vencedor="Candidato_Z"
    elif branco>nulo:
        vencedor="Votos em branco"
    elif nulo>x and nulo>y and nulo>z and nulo>branco:
        vencedor="Votos Nulos"
    else:
        if x==y or x==z or y==z:
            vencedor="Houve empate"
        elif nulo==branco:
            vencedor="Nulos e brancos"
        else:
            vencedor="Empate entre um candidato e brancos ou nulos"
    return vencedor


candidato_X=0
candidato_Y=0
candidato_Z=0
branco=0
nulo=0

while True:
    try:
        exibir_menu()
        voto=int(input("Olá, digite o número seu candidato"))
        opção=input("Deseja finalizar a votação ? (s/n)")
        if voto==889:
            candidato_X+=1
        elif voto==847:
            candidato_Y+=1
        elif voto==515:
            candidato_Z+=1
        elif voto==0:
            branco+=1
        else:
            nulo+=1

        if opção=="s":
            ganhador=apontar_vencendor(candidato_X,candidato_Y,candidato_Z,branco,nulo)
            break
        elif opção=="n":
            continue
    except ValueError:
        print("ERRO! Digite apenas números inteiros. Vote novamente")

print("O candidato vencedor foi: {} " .format(ganhador))
print("Candidato_X: {} votos" .format(candidato_X))
print("Candidato_Y: {} votos" .format(candidato_Y))
print("Candidato_Z: {} votos" .format(candidato_Z))
print("Votos em Braco: {} votos" .format(branco))
print("Votos Nulos: {} votos" .format(nulo))