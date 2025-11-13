def receberNotas():
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))

    def calcular_media(nota1, nota2):
        media = (nota1 + nota2) / 2
        return media
    
    

    def situacao(media):
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"
        
    media = calcular_media(nota1, nota2)
    status = situacao(media)
    return status

print(f"{receberNotas()}")