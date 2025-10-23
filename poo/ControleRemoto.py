class ControleRemoto:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

controle_remoto = ControleRemoto("preto", "samsung")

print(controle_remoto.cor)
print(controle_remoto.marca)