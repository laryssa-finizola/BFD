def processar_frase():
    frase_original = input("digite sua frase:")

    palavras = frase_original.split()

    numero_de_palavras = len(palavras)

    palavras_invertidas = palavras[:: -1]

    frase_invertida = " ".join(palavras_invertidas)

    print(f"A frase possui: {numero_de_palavras} palavras.")
    print(f"Frase invertida: {frase_invertida}")

processar_frase()