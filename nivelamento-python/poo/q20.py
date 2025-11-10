class Retangulo:
    def __init__(self,  largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura

r1 = Retangulo(5, 10)
print(f"Área do retângulo: {r1.area()}")