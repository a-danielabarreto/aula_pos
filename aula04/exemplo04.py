'''Situação Problema 04
Utilizando a lista de números criada na SP3, vamos
desenvolver uma solução que nos ajude a saber
quantos são pares e quantos são ímpares.

Direto para o PyCharm! *_*'''

from random import randint
lista_num = []

for i in range(100):
    numero_aleatorio = randint(0,1000)
    print(f'O número escolhido foi: {numero_aleatorio}')
    lista_num.append(numero_aleatorio)

print(lista_num)

#contadores
n_impar = 0
n_par = 0

for j in lista_num:

    if (j % 2) == 0:
        n_par += 1
    else:
        n_impar += 1
print(f'Esta lista tem {n_par} números pares e {n_impar} ímpares.')
