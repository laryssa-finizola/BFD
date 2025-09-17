numeroSecreto = int(input("Digite seu número = "))
testes_loop = [10, 30, 40, 50, 80, 100, 40, 50, 0, 90]

def tipoDeNumero():
    if numeroSecreto > 0:
        print(f"Seu número secreto ({numeroSecreto}) é positivo.")
    elif numeroSecreto < 0:
        print(f"Seu número secreto ({numeroSecreto}) é negativo.")
    else:
        print(f"Seu número secreto ({numeroSecreto}) é zero.")

def loopAteZero(lista):
    print("\nIniciando o loop...")
    for numero in lista:
        if numero != 0:
            print(f"Continue até chegar o 0. O número atual é: {numero}")
        else:
            print(f"Chegamos no 0! Loop encerrado.")
            break 

tipoDeNumero()
loopAteZero(testes_loop)