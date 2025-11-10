numero = int(input("Digite um número: "))

if numero > 10:
    print("numero maior que 10")
elif numero == 10:
    print("numero igual a 10")
else:
    print("numero menor que 10")






numero = int(input("Digite um número: "))

if numero > 0:
    print("numero positivo")
elif numero == 0:
    print("numero zero")
else:
    print("numero negativo")





numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("numero par")
else:
    print("numero impar")






idade = int(input("Digite um número: "))

if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")



senha = input("Digite a senha: ")
senha_correta = "123"

if senha == senha_correta:
    print("Senha correta!")
else:
    print("Senha incorreta!")




n1 = 5
n2 = 5

if n1 > n2:
    print(n1,"é maior")
elif n1 == n2:
    print(n1, "=", n2)
else:
    print(n2, "é maior")





n1 = 50
n2 = 500
n3 = 7

if n1 > n2 and n1 > n3:
    print(n1,"é maior")
elif n2 > n1 and n2 > n3:
    print(n2,"é maior")
else:
    print(n3,"é maior")






n1 = 5.00
n2 = 3.00

def media(n1, n2):
    return (n1 + n2) / 2

if media(n1, n2) >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")





idade = int(input("Digite um número: "))

if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")




turno = int(input("Digite o horário: "))

if 6 <= turno < 12:
    print("matutino")
elif 12 <= turno < 18:
    print("vespertino")
elif 18 <= turno < 24:
    print("noturno")
else:
    print("Turno inválido!")
