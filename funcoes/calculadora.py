numeroA = int(input("Digite o primeiro numero: "))
numeroB = int(input("Digite o segundo numero: "))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# chamada + impressãos
print(f"Soma = {soma(numeroA, numeroB)}")
print(f"Subtração = {subtracao(numeroA, numeroB)}")
print(f"Multiplicação = {multiplicacao(numeroA, numeroB)}")
print(f"Divisão = {divisao(numeroA, numeroB)}")