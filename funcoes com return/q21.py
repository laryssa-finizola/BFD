lista = ["python", "java", "c++", "javascript"]

def maior_string(lista):
    return max(lista, key=len)

print(maior_string(lista))