# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome=nome

    def set_ender(self, ender):
        self.ender=ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

    pessoa1 = Pessoa("maria","rua 01234")
    pessoa2 = Pessoa("joao","rua 56789")

    print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get.ender()}')
    print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')







