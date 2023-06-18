""" A partir do ano de nascimento de uma pessoa mostrar
sua idade, se já tem idade para votar (16 anos ou
mais) e se já pode ser candidato a uma carteira de
habilitação.
Dados de entrada: ano de nascimento
Saída: idade, idade para votar, idade para dirigir """

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = 2023 - ano_nascimento
print(f'Sua idade em 2023 é {idade} anos.')

if idade < 16:
    print('Você ainda não pode votar e nem dirigir!')

elif 16 <= idade < 18:
    print('Você pode votar, mas não pode dirigir!')

else:
    print('Você pode votar e dirigir!')