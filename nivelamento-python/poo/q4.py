class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

#objetos
c1 = Carro("fusca", "azul")
c2 = Carro("ferrari", "vermelha")

print(f" modelo: {c1.modelo}, cor: {c1.cor}")
print(f" modelo: {c2.modelo}, cor: {c2.cor}")