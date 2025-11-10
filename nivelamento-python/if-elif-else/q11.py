turno = int(input("Digite o horário: "))

if 6 <= turno < 12:
    print("matutino")
elif 12 <= turno < 18:
    print("vespertino")
elif 18 <= turno < 24:
    print("noturno")
else:
    print("Turno inválido!")
