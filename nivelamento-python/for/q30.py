numeros = []
contagem = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

    if num < 0:
        contagem += 1
        
print("Números digitados:", numeros)
print("Números negativos =", contagem)
