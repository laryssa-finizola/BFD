letra = input("Digite uma letra para verificar se está presente na palavra: ")
palavra = 'Glestiano'

indice = -1
for i in range(len(palavra) ):
    if palavra[i] == letra:
        indice = i
        break

if indice != -1:
    print(f"A letra '{letra}' aparece pela primeira vez no índice {indice}.")
else:
    print(f"A letra '{letra}' não está presente na palavra.")
