# fatorial de um numero = n! = n * (n-1) * (n-2) * ... * 1

n = int(input("Digite um número inteiro: "))

def fatorial(n):
    if n < 0:
        return "Fatorial não é definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        ##


