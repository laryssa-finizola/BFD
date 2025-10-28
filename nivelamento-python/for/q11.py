palavra = "python é a melhor linguagem" #esperado = 4
contagem = 0
espaco = " "

for i in palavra:
    if i.lower() in espaco:
        contagem += 1

print (f"A palavra {palavra} possui {contagem} espaços")
