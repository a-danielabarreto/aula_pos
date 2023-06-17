'''Situação Problema 03
Vamos nos preparar para a situação problema número
quatro. Para isso, precisamos criar uma lista com
100 números inteiros e randômicos.

Já consegue imaginar como será nossa solução?'''

from random import randint

lista_num = []
controle = 0

while controle < 100:
    numero_aleatorio = randint(0, 1000)
    print(f'O número escolhido foi: {numero_aleatorio}')
    lista_num.append(numero_aleatorio)
    controle += 1

print(lista_num)