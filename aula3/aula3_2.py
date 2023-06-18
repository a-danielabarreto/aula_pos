''' Condição para cada função
1 - Adicionar pessoas
2 - Pesquisar uma pessoa '''

lista = ['Ana', 'Bruna', 'Carol', 'Daniela']


while True:

    print('1 - Adicionar\n2 - Pesquisar\n3 - Listar\n4 - Remover\n5 - Alterar')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        nome_pessoa = input('Digite o nome da pessoa: ')
        lista.append(nome_pessoa)

    elif opcao == 2:
        nome_pesquisa = input('Digite o nome a pesquisar: ')
        if nome_pesquisa in lista:
            print(f'O nome {nome_pesquisa} está na lista.')

    elif opcao == 3:
        for nome in lista:
            print(f'-> {nome}')

    elif opcao == 4:
        nome_remover = input('Digite quem será removido: ')
        if nome_remover in lista:
            lista.remove(nome_remover)
        else:
            print('Nome não entrado!')

    elif opcao == 5:
        nome_alterar = input('Digite quem será alterado: ')

        if nome_alterar in lista:
            print(f'O nome {nome_alterar} foi encontrado.')
            alteracao = input('Qual será o novo nome? ')
            lista[lista.index(nome_alterar)] = alteracao
        else:
            print('O nome não foi encontrado!')













