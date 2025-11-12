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


temperatura = 36.5

if temperatura > 37.5:
    print("Febre alta") 
elif temperatura <= 37.0 and temperatura >= 36.0:
    print("Febre leve")
else:
    print("Temperatura normal")




turno = int(input("Digite o horário: "))

if 6 <= turno < 12:
    print("matutino")
elif 12 <= turno < 18:
    print("vespertino")
elif 18 <= turno < 24:
    print("noturno")
else:
    print("Turno inválido!")




velocidade = 100

if velocidade > 80:
    print("velocidade alta") 
elif velocidade <= 80 and velocidade >= 60:
    print("velocidade normal")
else:
    print("velocidade baixa")






numero = int(input("Digite um número: "))

if numero > 0 and numero <= 100:
    print(numero, "está entre 0 e 100")
else:
    print(numero, "não está entre 0 e 100")



palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite uma palavra: ")

if palavra1 == palavra2:
    print("As palavras são iguais.") 
else:
    print("As palavras são diferentes.")







letra = input("Digite uma letra: ")

vogal =  ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")








a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print(f"{a} é maior que {b}")
elif a == b:
    print(f"{a} é igual a {b}")
else:
    print(f"{a} é menor que {b}")




l1 = int(input("digite o primeiro lado do triângulo: "))
l2 = int(input("digite o segundo lado do triângulo: "))
l3 = int(input("digite o terceiro lado do triângulo: "))

if l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")


if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Operação inválida")






""" Um ano é bissexto se for divisível por 400;

Ou se for divisível por 4, mas não por 100;

Caso contrário, não é bissexto. """

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print(f"{ano} é um ano bissexto.")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")





numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("o número é divisível por 3 e 5")
else:   
    print("o número não é divisível por 3 e 5")



