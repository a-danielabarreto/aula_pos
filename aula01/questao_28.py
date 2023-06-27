""" 28. [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo
que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raízes reais). """

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = (b ** 2) - (4 * a * c)

raiz1 = (-b + ( delta ** 0.5)) / (2 * a)
raiz2 = (-b - ( delta ** 0.5)) / (2 * a)

print(f'As raízes da equação são: {raiz1:0.2f}, e: {raiz2:0.2f}')