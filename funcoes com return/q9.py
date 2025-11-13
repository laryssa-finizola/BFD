a = int(input("digite um numero: "))
b = int(input("digite outro numero: "))

def resto_divisao(a, b):
    if a > b and b != 0:
        return a % b
    else:
        return "Não é possível calcular o resto da divisão."
    
print(resto_divisao(a, b))