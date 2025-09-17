idade = int(input("Digite sua idade: "))


if idade < 13:
    print("👶 Você é uma criança.")
elif idade < 18 and idade > 12:
    print("👩 Você é um adolescente.")
else:
    print("👨‍🔧Você é um adulto.")