altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso em kg (ex: 70.5): "))

imc = peso / (altura ** 2)
print(imc)