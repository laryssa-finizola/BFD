class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

aluno1 = Aluno(nome, nota)
print(f"Aluno: {aluno1.nome}, Nota: {aluno1.nota}")