lista = [10, 2, 39, 8, 93, 23, 22, 44, 57, 48]

def maior_diferenca(lista):
    maior = max(lista)
    menor = min(lista)
    return maior - menor
    
print(maior_diferenca(lista))