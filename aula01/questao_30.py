""" 30. [FORBELLONE, 2022] Faça um algoritmo para calcular o volume de uma esfera de raio R, em que R é um dado
fornecido pelo usuário. O volume da esfera é dado por 𝑉 = 4/3 ℼ𝑅3 """

raio = float(input('Digite o valor do raio da esfera em metros: '))
PI = 3.1415

volume = (4/3) * PI * (raio ** 3)

print(f'O volume da esfera é de: {volume:0.2f} metros')