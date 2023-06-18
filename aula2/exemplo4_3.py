""" Alterando o problema anterior, fazendo estruturas de seleção encadeada homogênea """

idade = int(input('Digite a sua idade: '))
tipo_ingresso = input('Digite o tipo de ingresso: VIP ou PISTA: ')
tipo_ingresso = tipo_ingresso.upper()

if idade >= 18 and tipo_ingresso == 'VIP':
    print('Pode entrar na festa!')
    print('Pode seguir para o primeiro andar.')

elif idade >= 18 and tipo_ingresso == 'PISTA':
    print('Pode entrar na festa!')
    print('Pode seguir para a pista!')

else:
    print('Não pode entrar na festa')

print('--- Fim do programa ---')