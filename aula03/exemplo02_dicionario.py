# Definição de um dicionário (declaração em uma linha ou em várias linhas)
professor = {
    'nome': 'Messias',
    'idade': 36
}

# Imprimindo os valores
print(professor['nome'])
print(professor['idade'])

aluno = {'nome': 'Aluno1', 'idade': 123}
print(aluno['nome'])

professores = {
    'Messias': {
        'idade': 36,
        'disciplinas': ['Introdução', 'Java']},
    'Daniela': {
        'idade': '32',
        'disciplinas': ['BD I', 'BD II']}
}

# Acessando valores no meu dicionário
print(f'O professor Messias tem {professores["Messias"]["idade"]} anos e ministra as disciplinas de {professores["Messias"]["disciplinas"][0]}')

# Adicionando novos valores
professores['Messias']['email'] = 'mrafaelbatista@gmail.com'
professores['Messias']['cpf'] = '000.000.000-00'

print(professores['Messias'])

# Tipos primitivos de dados: int, float, string, boolean
# Tipos novos: lista, tupla, dicionário

# Removendo valores
del professores['Messias']['cpf']

print(professores['Messias'])

print(type(professores))

print(professores.keys())
print(professores.items())

print(type(professores.keys()))
print(type(professores.items()))