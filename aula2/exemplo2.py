''' Precisamos de um programa de computador que calcule a quantidade de
latas de tinta e o custo total para pintar tanques cilíndricos de
combustível.
Sabemos que:
● A lata de tinta custa R$ 50,00
● Cada lata contém 5 litros
● Cada litro de tinta pinta 3 metros quadrados
● O custo = quantidade de latas * R$ 50,00
● A quantidade latas = a quantidade total de litros / 5
● A quantidade total de litros = área do cilindro / 3
● Área do cilindro = área da base + área lateral
● Área da base = PI * (R ** 2)
● Área lateral = altura * comprimento (2 * PI * R * H)
● Sendo que R (raio) e H (altura) são dados de entrada e PI é
uma constante de valor 3,14. '''

import math

PI = 3.14
r = float(input('Digite o raio da base do cilindro: '))
h = float(input('Digite a altura da base do cilindro: '))

area_lateral = (2 * PI * r * h)
area_base = PI * (r ** 2)
area_cilindro = area_lateral + area_base
quantidade_total_litros = area_cilindro / 3
quantidade_latas = math.ceil(quantidade_total_litros / 5)
custo = quantidade_latas * 50.0

print(f'A quantidade total de litros é de {quantidade_total_litros:0.2f} e o custo total é de R$ {custo:0.2f}.')
print (f'A quantidade de latas é de {quantidade_latas}')