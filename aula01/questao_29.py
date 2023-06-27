""" 29. [FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, P(𝑥1,
𝑦1 ) e Q(x2, y2), imprima a distância entre eles.
a. A fórmula que efetua tal cálculo é: 𝑑 = (𝑥2 − 𝑥1)2 + (𝑦2 − 𝑦1)2 """

x1 = float(input('Digite o valor de x1: '))
y1 = float(input('Digite o valor de y1: '))
x2 = float(input('Digite o valor de x2: '))
y2 = float(input('Digite o valor de y2: '))

distancia = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

print(f'A distância é de: {distancia:0.2f}')