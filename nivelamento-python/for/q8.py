palavra = "computador" #esperado = 4
contagem = 0
vogais = "aeiou"

for i in palavra:
    if i.lower() in vogais:
        contagem += 1

print (f"A palavra {palavra} possui {contagem} vogais")
