class Pessoa:
    def __init__(self, nome, idade, carteira):
        self.nome = nome
        self.idade = idade
        self.carteira = carteira


primeira_pessoa = Pessoa("Laryssa", 23, False)

print(f"Nome = {primeira_pessoa.nome}")
print(f"Idade = {primeira_pessoa.idade} anos")
print(f"Cateira = {primeira_pessoa.carteira}")