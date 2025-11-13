texto = "python é uma linguagem de programação"
letra = "a"

def ocorrencia(texto, letra):
    contador = 0
    for i in texto:
        if i == letra:
            contador += 1
    return contador

print(ocorrencia(texto, letra))