nome = "Laryssa"


print(nome[0])





palavra = 'Glestiano'

print(f"A última letra de '{palavra}' é: {palavra[-1]}")






palavra = 'Glestiano'

print(f"A terceira letra de '{palavra}' é: {palavra[2]}")






palavra = 'Glestiano'

print(f"A terceira letra de '{palavra}' é: {palavra[-2]}")







palavra = 'Glestiano'

for i in range(len(palavra)):
    print((palavra[i]))






palavra = 'Glestiano'
contem = "a"

if contem in palavra:
    print(f"A letra '{contem}' está presente na palavra '{palavra}'.")




palavra = 'Glestiano'
contem = "x"

if contem in palavra:
    print(f"A letra '{contem}' está presente na palavra '{palavra}'.")
else:
    print(f"A letra '{contem}' NÃO está presente na palavra '{palavra}'.")












palavra = 'Glestiano'
substring = "iano"

if substring in palavra:
    print(f"A substring '{substring}' está presente na palavra '{palavra}'.")
else:
    print(f"A substring '{substring}' NÃO está presente na palavra '{palavra}'.")








palavra = 'Glestiano'
substring = "tes"

if substring in palavra:
    print(f"A substring '{substring}' está presente na palavra '{palavra}'.")
else:
    print(f"A substring '{substring}' NÃO está presente na palavra '{palavra}'.")






palavra = 'Glestiano'
letra = input("Digite uma letra para verificar se está presente na palavra: ")

if letra in palavra:
    print(f"A letra '{letra}' está presente na palavra '{palavra}'.")
else:
    print(f"A letra '{letra}' NÃO está presente na palavra '{palavra}'.")








palavra = 'Glestiano'
contem = "z"

if contem in palavra:
    print(f"A letra '{contem}' está presente na palavra '{palavra}'.")
else:
    print(f"A letra '{contem}' NÃO está presente na palavra '{palavra}'.")






palavra = 'Glestiano'
contem = "G"

if contem in palavra:
    print(f"A letra '{contem}' está presente na palavra '{palavra}'.")
else:
    print(f"A letra '{contem}' NÃO está presente na palavra '{palavra}'.")







palavra = 'Glestiano'
contem = "ano"

if contem in palavra:
    print(True)
else:
    print(False)







palavra = 'Glestiano'
contem = "abc"

if contem not in palavra:
    print("está ausente")
else:
    print("está presente")





