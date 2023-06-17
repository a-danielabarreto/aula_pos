from random import randint
lista_num = []

for i in range(100):
    numero_aleatorio = randint(0,1000)
    print(f'O número escolhido foi: {numero_aleatorio}')
    lista_num.append(numero_aleatorio)

print(lista_num)