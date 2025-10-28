class Carro:
    def __init__(self, estado="novo"):
        self.estado = estado

#objetos
fusca = Carro("novo")
ferrari = Carro("usado")

print(fusca.estado)
print(ferrari.estado)