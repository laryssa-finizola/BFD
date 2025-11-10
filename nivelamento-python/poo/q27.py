class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Pessoa {self.nome} criada com idade {self.idade}")

# Objetos
p1 = Pessoa("Ana", 30)
p2 = Pessoa("Maria", 25)
