class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Adriana", 25)
p1.apresentar()


# Mesmo exemplo, criando várias pessoas com 'input()' -> inserindo dados

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

pessoa = Pessoa(nome, idade)
pessoa.apresentar()
