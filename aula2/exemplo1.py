""" Construir um algoritmo que calcule a média aritmética entre
quatro notas bimestrais fornecidas por um aluno (usuário).
Dados de entrada: quatro notas (n1, n2, n3, n4)
Dados de saída: média aritmética anual (ma) """

n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
n3 = float(input('Digite o valor da terceira nota: '))
n4 = float(input('Digite o valor da quarta nota: '))

media_anual = (n1 + n2 + n3 + n4) / 4

print(f'A média anual é de: {media_anual:0.1f}')