class Produto: 
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem / 100)
        return self.preco - desconto
    
produto1 = Produto("camisa", 80)
desconto = produto1.calcular_desconto(10)
    
print(f"Nome: {produto1.nome},Preço sem desconto: {produto1.preco}, Preço com desconto: {desconto}")