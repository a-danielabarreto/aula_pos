# Declarando uma lista

nomes = ['Messias', 'Verônica', 'Miguel', 'Gabriela']

print(nomes)

print(f'O tipo do dado é: {type(nomes)}')

print(f'Imprimindo a posição 0: {nomes[0]}')

print ('--- Frutas ---')

frutas = ['pêra', 'uva', 'maçã', 'kiwi']

print(frutas)

frutas[1] = 'abacate'

print(frutas)

# Não é a forma mais usual. (posição, valor)

frutas.insert(2, 'morango')

print(frutas)

frutas.insert(1, 'pitanga')

frutas.insert(5, 'graviola')

print(frutas)

del frutas[1]

del frutas[4]

print(frutas)

frutas.insert(5, 'melancia')

indice_melancia = frutas.index('melancia')

print(f'O índice da melancia é {indice_melancia}')

del frutas[indice_melancia]

frutas.remove('kiwi')

print(frutas)

print(len(frutas))  # Mostra a quantidade de elementos da lista

print(len('Daniela Barrêto'))

frutas.insert(2,'abacaxi')

print(frutas)

indice_abacaxi = frutas.index('abacaxi')

abacaxi_pop = frutas.pop(indice_abacaxi)

print(frutas)

print(f'A fruta deletada foi: {abacaxi_pop}')

frutas.append('pitaya') # Adiciona elemento ao final da lista

print(frutas)






