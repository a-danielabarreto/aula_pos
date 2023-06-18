nome = "daniela barreto"
print(nome)
print('Estudando para ser programadora')

input('Digite seu nome: ')
int(input("Digite sua idade: "))

print(nome.title())
print(nome.upper())
print(nome.lower())

primeiro_nome = 'Daniela'
segundo_nome = 'Barrêto'
nome_completo = primeiro_nome + ' ' + segundo_nome
print(nome_completo)
print('Olá, ' + nome_completo.title())
print("\tDaniela Barrêto")
print("Harry\nHermione\nRone")

professor = " Dumbludore"

print(professor)
print(professor.rstrip())
print(professor.lstrip())
print(professor.strip())

ano = 2022
print(f'Este ano de {ano} será maravilhoso!')

pi = 3.141414141414
print("O valor de PI é {:0.2f}".format(pi))

altura = 1.77
print(f"O valor de PI é {altura:0.2f}")

idade = 18
print('Eu tenho %d anos' % idade)

nome = 'messias'
print('Meu nome é %s' % nome)

fruta = 3.7543
print('O abacate custa R$ %.2f' % fruta)