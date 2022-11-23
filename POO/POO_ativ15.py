'''
  Crie uma situação em que ocorra uma exceção dentro de um código. Utilize try/catch para realizar a captura e tratamento dessa exceção. 
'''


lista = [1, 2, 3]
numero = int(input(f'Digite um número entre 0 e {len(lista)-1}: '))
try:
    print(lista[numero])
except IndexError:
    print('O número digitado está fora da faixa aceita')