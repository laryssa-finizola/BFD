palavra = 'Glestiano'
letra = input("Digite uma letra para verificar se está presente na palavra: ")

if letra in palavra:
    print(f"A letra '{letra}' está presente na palavra '{palavra}'.")
else:
    print(f"A letra '{letra}' NÃO está presente na palavra '{palavra}'.")