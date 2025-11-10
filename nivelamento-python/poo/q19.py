class Carro:
    def __init__(self,  marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano do carro: ")

carro = Carro(marca, modelo, ano)
print(f"Carro criado: {carro.marca} {carro.modelo} {carro.ano}")