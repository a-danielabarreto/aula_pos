""" 8. Exercício da Conversão de Moedas: Escreva um programa em Python que solicite ao usuário um valor em Real (BRL) e
faça a conversão desse valor para Dólar Americano (USD). Considere a taxa de câmbio fixa de 1 USD = 5 BRL. Exiba o
valor convertido na tela. """

real = float(input('Digite o valor em Real (BRL): '))

dolar = real / 5

print('O valor em dolar americano é: USD %.2f' %dolar)