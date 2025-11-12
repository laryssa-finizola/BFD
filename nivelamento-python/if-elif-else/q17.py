l1 = int(input("digite o primeiro lado do triângulo: "))
l2 = int(input("digite o segundo lado do triângulo: "))
l3 = int(input("digite o terceiro lado do triângulo: "))

if l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
