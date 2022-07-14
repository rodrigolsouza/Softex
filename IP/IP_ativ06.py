'''Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo para algum repositório e compartilhe o link no campo ao lado para que outros desenvolvedores possam analisá-lo.'''

rodas= int(input("Digite o número de rodas do seu veículo: "))
pesoVeiculo=int(input("Digite o peso do seu veículo em Kg: "))
capacidade=int(input("Digite a capacidade máxima de pessoas que seu veículo transporta: "))

categoria=""

if rodas==2 or rodas==3:
    categoria="A"
elif rodas==4 and capacidade<=8 and pesoVeiculo<3500:
    categoria="B"
elif rodas>=4 and (pesoVeiculo>=3500 and  pesoVeiculo<=6000):
    categoria="C"
elif rodas>=4 and capacidade>8:
    categoria="D"
elif rodas>=4 and pesoVeiculo>6000:
    categoria="E"
else:
    print("opção inválida! Digite um número de rodas válido")
print("A melhor categoria que seu veículo se encaixa é: {}" .format(categoria))