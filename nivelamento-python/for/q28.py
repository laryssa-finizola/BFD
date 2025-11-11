numeros = [8, 5, 7, 0, 9, 5, 6, 0, 10, 0]

maior_num = numeros[0]
menor_num = numeros[0]


for i in numeros:
    if i > maior_num:
        if i %2 != 0:
            maior_num = i


print(f"Lista de Números: {numeros}")
print(f"Maior número ímpar: {maior_num}")