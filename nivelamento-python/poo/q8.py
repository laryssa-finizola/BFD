class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#objetos
produto1 = Produto("mouse", 200)
produto2 = Produto("teclado", 300)
produto3 = Produto("monitor", 800)


#chamada de método
print(f"Nome: {produto1.nome}, Preço: {produto1.preco}")
print(f"Nome: {produto2.nome}, Preço: {produto2.preco}")
print(f"Nome: {produto3.nome}, Preço: {produto3.preco}")