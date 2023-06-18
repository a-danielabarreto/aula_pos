""" Exercício do IMC (Índice de Massa Corporal): Escreva um programa em Python que solicite ao usuário sua altura em
metros e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura *
altura). Exiba o resultado do IMC na tela. """

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilogramas: '))

imc = peso / (altura * altura)

print('O seu IMC é de: %.2f' %imc)