class Banco: 
    def __init__(self, clientes):
        self.clientes = clientes 

# Objetos
clientes = Banco(["Ana", "Maria", "José"])     

print(f"Clientes do banco: {clientes.clientes}")