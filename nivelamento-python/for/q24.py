numero = int(input("Digite um número inteiro positivo: "))
divisores = []
if numero > 0:
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    
    print(f"Os divisores de {numero} são: {divisores}")
else:
    print("Por favor, digite um número inteiro positivo.")
