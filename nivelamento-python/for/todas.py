for i in range(1,11):
    print(i)



for i in range(1, 21):
    if i % 2 == 0:
        print(i)  


numeroSecreto = int(input("informe seu número"))

for i in range (0, 11):
    resultado = i * numeroSecreto
    print (f"{numeroSecreto} x  {i}  = {resultado}")


soma = 0

for i in range(1, 101):
    soma = soma + i
    i += 1;  

print(soma)



palavra = "ola"

for i in palavra:
    print (i)


palavra = "computador" #esperado = 4
contagem = 0
vogais = "aeiou"

for i in palavra:
    if i.lower() in vogais:
        contagem += 1

print (f"A palavra {palavra} possui {contagem} vogais")


soma = 0

for i in range(10):
    numero = int(input(f"digite o {i} numero = "))
    soma += numero

print(soma)
media = soma / 10
print(f"Média total dos números = {media}")


fatorial = 1
for i in range(1, 6): #sempre um numero além
    fatorial = fatorial * i

print(fatorial) 



palavra = "python é a melhor linguagem" #esperado = 4
contagem = 0
espaco = " "

for i in palavra:
    if i.lower() in espaco:
        contagem += 1

print (f"A palavra {palavra} possui {contagem} espaços")


