class Carro: 
    def __init__(self, estado):
        self.estado = estado

    def mostrar_estado(self):
        return self.estado
    
#objetos 
c1 = Carro("novo")
c2 = Carro("semi novo")

print(f"Estado do carro 1: {c1.mostrar_estado()}")
print(f"Estado do carro 2: {c2.mostrar_estado()}")