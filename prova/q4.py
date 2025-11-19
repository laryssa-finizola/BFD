class Produto:
    def __init__(self, preco):
        self.preco = preco

    def desconto_percentual(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto
    
#objetos
p1 = Produto(200)
print(p1.desconto_percentual(10))

