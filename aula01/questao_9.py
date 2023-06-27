""" 9. Exercício do Volume de uma Esfera: Escreva um programa em Python que solicite ao usuário o raio de uma esfera.
Calcule o volume dessa esfera usando a fórmula V = (4/3) * pi * r³, onde pi é uma constante aproximada de 3.1415. Exiba
o volume calculado na tela. """

raio = float(input('Digite o raio da esfera: '))
PI = 3.1415

volume = (4/3) * PI * (raio ** 3)

print('O volume da esfera é de: %.2f' %volume)
