""" 4. Exercício do Desconto: Escreva um programa em Python que solicite ao usuário o valor de um produto e o percentual de
desconto. Calcule o valor do desconto e exiba o valor final após o desconto. """

valor = float(input('Digite o valor do produto: '))
percentual = float(input('Digite o percentual de desconto em decimal: '))

desconto = valor * percentual
resultado = valor - desconto
print('O valor final do produto é: R$ %.2f' %resultado)

