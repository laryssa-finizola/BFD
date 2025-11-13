texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"


def contar_vogais(texto):
    contator = 0
    for letra in texto:
        if letra in vogais:
            contator += 1
    return contator

print(f"O número de vogais no texto é: {contar_vogais(texto)}")