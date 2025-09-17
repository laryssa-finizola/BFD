nota1 = float(input("nota 1:"))
nota2 = float(input("nota 2:"))

media = nota1/ nota2

if (media >= 7):
    print("aluno aprovado")
elif(media >= 4 and media < 7):
    print("aluno irá para a final")
else: 
    print("aluno reprovado")
