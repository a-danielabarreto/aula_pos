""" Alterando o problema anterior, fazendo estruturas de seleção encadeada homogênea """

idade = int(input('Digite a sua idade: '))

if 17 < idade < 100:
    print('Pode ir ao guichê!')
    tipo_ingresso = input('Digite o tipo de ingresso: VIP ou PISTA: ')
    tipo_ingresso = tipo_ingresso.upper()
    print(f'Seu tipo de ingresso é {tipo_ingresso}')

    if tipo_ingresso == 'VIP':
        print('Pode seguir para o PRIMEIRO ANDAR!')
    elif tipo_ingresso == 'PISTA':
        print('Vá em direçao a PISTA!')
else:
    print('Você não tem a idade permitida!')

print('--- Fim do programa ---')