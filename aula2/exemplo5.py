""" Um programa que permita saber qual o peso ideal de
uma pessoa.
● Para homens: (72,7 * h) - 58
● Para mulheres: (62,1 * h) - 44,7
Dados de entrada: altura e sexo de uma pessoa. """

altura = float(input('Digite a sua altura em metros: '))
genero = input('Digite seu gênero (M ou F): ').upper()

if genero == 'M':
    peso_ideal = (72.7 * altura) - 58

elif genero == 'F':
    peso_ideal = (62.1 * altura) - 44.7

else:
    print('Dados de entrada não encontrados (dados válidos: M ou F)')

print(f'Você que é do gênero {genero} tem peso ideal igual a {peso_ideal:0.2f} kg')