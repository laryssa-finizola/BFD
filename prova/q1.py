class Carro:
    def __init__(self, estado):
        self.estado = estado

    def mostrar_estado(self):
        return f"O carro está {self.estado}."

#objetos
c1 = Carro("ligado")
print(c1.mostrar_estado())

c2 = Carro("desligado")
print(c2.mostrar_estado())