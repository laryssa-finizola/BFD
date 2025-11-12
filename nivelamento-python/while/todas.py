i = 1 

while i <= 10:
    print (i)
    i += 1





i = 10

while i <= 10 and i >= 1:
    print (i)
    i -= 1




i = 0
while i >= 0 and i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


i = 1
while i >= 1 and i <= 19:
    if i % 2 != 0:
        print(i)
    i += 1


numero = int(input("Digite um número: "))
i = 1
while i >= 1 and i <= numero:
    print(i)
    i += 1


palavra = input("Digite uma palavra: ")
i = 1
while i <= 5:
    print(palavra)
    i += 1


i = 0

while i <= 10:
    print(f"2 x {i} = {2 * i}")
    i += 1


i = 0
numero = int(input("Digite um número: "))

while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1




i = 1

while i <= 5:
    nome = input("Digite um nome: ")
    print(nome)
    i += 1



i = 1
nomes = []
while i <= 5:
    nome = input("Digite um nome: ")
    nomes.append(nome)
    i += 1

print(nomes)