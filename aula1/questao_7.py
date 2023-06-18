""" 7. Exercício do Tempo de Viagem: Escreva um programa em Python que solicite ao usuário a distância de uma viagem (em
km) e a velocidade média (em km/h). Calcule o tempo de viagem em horas e exiba o resultado. """

distancia = float(input('Digite a distância em km: '))
velocidade = float(input('Digite a velocidade média em km/h: '))

tempo = distancia / velocidade

print('O tempo de viagem em horas é de: %.2f' %tempo+ ' horas')