#codigo para exemplificar o uso de operadores lógicos

#uso do and 
idade = int(input("digite sua idade: "))
emancipado = input("você é emancipado?").lower()

if idade < 16 and idade > 12:
    print("desculpe, não é possível participar.")


#uso do or
if idade >= 16 or emancipado == "sim":
    print("você está apto a participar!")

##uso do not 
if not idade >= 18 and emancipado == "não":
    print("desculpe, não está apto a participar.")