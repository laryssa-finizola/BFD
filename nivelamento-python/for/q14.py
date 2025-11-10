notas = [8.5, 7.0, 9.5, 6.0, 10.0]

maior_nota = notas[0]
menor_nota = notas[0]


for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
        
    if nota < menor_nota:
        menor_nota = nota


print(f"Lista de Notas: {notas}")
print(f"Maior nota: {maior_nota:.1f}")
print(f"Menor nota: {menor_nota:.1f}")