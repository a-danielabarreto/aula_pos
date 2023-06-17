def calculadora(n1, n2):

    resultado_soma = n1 + n2
    resultado_subtracao = n1 - n2
    resultado_multiplicacao = n1 * n2
    resultado_divisao = n1 / n2

    return resultado_soma, resultado_subtracao, resultado_multiplicacao, resultado_divisao

# print(calculadora(10, 20))

soma, subtracao, multiplicacao, divisao = calculadora(10, 20)

print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')


