soma = 0

for i in range(10):
    numero = int(input(f"digite o {i} numero = "))
    soma += numero

print(soma)
media = soma / 10
print(f"Média total dos números = {media}")