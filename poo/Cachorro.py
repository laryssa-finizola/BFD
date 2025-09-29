class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

meu_cachorro = Cachorro("Max", 2)

print(f"Meu cachorro se chama {meu_cachorro.nome}")
print(f"Meu cachorro tem {meu_cachorro.idade} anos")

# explicações: 
# 
#    __init__ = é o construtor do objeto, ou seja, é um método especial
#    que é chamado automaticamente toda vez que você cria um novo objeto
#    de uma classe.

#  self = é uma referência ao próprio objeto que está sendo criado. Ele é o primeiro parâmetro 
#  de qualquer método de uma classe e é usado para acessar os atributos e outros métodos desse
#  objeto.
#
#