# hipotenusa = (cateto1**2 + cateto2**2)**0.5

cateto1 = float(input("Digite o comprimento do primeiro cateto: "))
cateto2 = float(input("Digite o comprimento do segundo cateto: "))

def calcular_hipotenusa(cateto1, cateto2):
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa

print(f"A hipotenusa é: {calcular_hipotenusa(cateto1, cateto2):.2f}")