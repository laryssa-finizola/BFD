minutos = int(input("Digite o tempo em minutos: "))

def conversor_tempo(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return f"{horas}h {minutos_restantes}min"

print(conversor_tempo(minutos))
