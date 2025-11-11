frase = "hoje tive aula de python"

contador = 0

for letra in frase:
    if letra == "a":
        contador += 1

print(f"A letra 'a' aparece {contador} vezes na frase.")