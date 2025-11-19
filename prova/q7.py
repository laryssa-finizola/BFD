def soma_pares(lista):
    for i in lista:
        if i % 2 == 0:
            soma = sum(lista)
    return soma

print(soma_pares([1,2, 3, 4, 5]))