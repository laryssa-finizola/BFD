lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def somar_pares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    return soma

print(somar_pares(lista))