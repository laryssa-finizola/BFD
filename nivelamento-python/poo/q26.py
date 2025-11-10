class Casa: 
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

# Objetos
c1 = Casa("azul", "grande")
c2 = Casa("vermelha", "pequena")

print(f"Casa 1 - Cor: {c1.cor}, Tamanho: {c1.tamanho}")
print(f"Casa 2 - Cor: {c2.cor}, Tamanho: {c2.tamanho}")
