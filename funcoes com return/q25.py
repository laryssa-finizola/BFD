valor = float(input("Digite um valor em reais: "))
desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))

def calcular_desconto(valor, desconto):
    valor_desconto = valor * (desconto / 100)
    valor_final = valor - valor_desconto
    return valor_final

print(f"{calcular_desconto(valor, desconto):.2f}")