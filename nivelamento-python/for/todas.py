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


nomes = ["Ana", "João", "Maria", "José", "Ricardo"]
nomes_invertidos = reversed(nomes)

for nome in nomes_invertidos:
    print(nome)





notas = [8.5, 7.0, 9.5, 6.0, 10.0]

maior_nota = notas[0]
menor_nota = notas[0]


for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
        
    if nota < menor_nota:
        menor_nota = nota


print(f"Lista de Notas: {notas}")
print(f"Maior nota: {maior_nota:.1f}")
print(f"Menor nota: {menor_nota:.1f}")






for i in range(1, 30):
    if i % 2 != 0:
        print(i)






for i in range(1, 11):
    quadrado = i ** 2
    print(f"{i} ** 2  = {quadrado}")






entrada = []
positivos = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))
    entrada.append(numero)

    if numero % 2 == 0:
        positivos.append(numero)

print("Lista de todos os números:", entrada)
print("Números pares:", positivos)






palavra_original = "palavra"
palavra_invertida = ""

# Itera sobre cada caractere na palavra original
for caractere in palavra_original:
    palavra_invertida = caractere + palavra_invertida

print(f"A palavra invertida de {palavra_original} é {palavra_invertida}")




numeros = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]


for numero in numeros:
    if numero % 2 == 0:
        print(numero)




lista_elementos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


for indice in range(len(lista_elementos)):
    
    # 2. Acessa o elemento usando o índice gerado
    elemento = lista_elementos[indice]
    
    print(f"Índice: {indice} | Elemento: {elemento}")






print("Contagem regressiva de 10 a 1:")
for numero in range(10, 0, -1):
    print(numero)















