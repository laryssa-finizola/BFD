class Banco:
    def __init__(self, clientes):
        self.clientes = clientes

#objetos
b1 = Banco(["joão", "maria", "ana"])
print(b1.clientes)