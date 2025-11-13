peso = 60
altura = 1.75

def imc(peso, altura):
    return peso / (altura ** 2)

print(f"{imc(peso, altura):.2f}")