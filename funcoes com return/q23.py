lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def filtrar_pares(lista):
    lista_pares = []
    for n in lista:
        if n % 2 == 0:
            lista_pares.append(n)
    return lista_pares

print(filtrar_pares(lista))