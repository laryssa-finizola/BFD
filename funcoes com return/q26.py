nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

def calcular_media(nota1,nota2):
    media = (nota1 + nota2) / 2
    if media >= 7:
        return "Aprovado"
    else: 
        return "Reprovado"
    
print(calcular_media(nota1, nota2))