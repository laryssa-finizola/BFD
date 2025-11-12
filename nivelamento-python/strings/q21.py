nome = "Glestiano"
letra = "a"
contador = 0


for i in range(len(nome)):
    if nome[i] == letra:
        contador += 1

print(contador)


""" 
outro modo mais eficiente:

nome = "Glestiano"
letra = "a"
contador = nome.count(letra)
print(contador)


"""