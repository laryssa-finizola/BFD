def numero_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro maior que 1: "))
print(numero_primo(n))
