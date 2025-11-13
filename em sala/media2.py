def receberNotas ():
    nota1 = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota: "))
    return ((nota1 + nota2))

def media():
    media = receberNotas()/2
    return media

print(media())