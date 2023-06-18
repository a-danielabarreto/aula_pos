""" 5. Exercício da Conversão de Temperatura: Escreva um programa em Python que solicite ao usuário uma temperatura em
graus Celsius e faça a conversão para Fahrenheit. Exiba o resultado na tela. """

celsius = float(input('Digite a temperatura em graus Celsius: '))

fahrenheit = celsius * 1.8 + 32

print('O valor da temperatura em Fahrenheit é: %.2f graus Fahrenheit' %fahrenheit)