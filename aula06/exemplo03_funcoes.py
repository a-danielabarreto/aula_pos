import minhas_funcoes
from random import randint

while True:
    op = input('Digite a opção: \n1 - Somar\n2 - Subtrair\n3 - Sair')
    op = int(op)

    match op:
        case 1:
           resultado = minhas_funcoes.somar(randint(1, 5), randint(1, 5))
           print(f'A soma foi: {resultado}')
        case 2:
            resultado = minhas_funcoes.subtrair(randint(100, 200), randint(100, 200))
            print(f'A subtração foi: {resultado}')
        case 3:
            break
        case _:
            print(f'Opção Inválida!')