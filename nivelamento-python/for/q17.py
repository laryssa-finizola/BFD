entrada = []
positivos = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    entrada.append(numero)

    if numero % 2 == 0:
        positivos.append(numero)

print("Lista de todos os números:", entrada)
print("Números pares:", positivos)
