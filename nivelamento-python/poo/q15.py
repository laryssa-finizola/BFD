class Aluno:   
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso



a1 = Aluno("Ana", "Ciência da Computação")
a2 = Aluno("Pedro", "Análise e Desenvolvimento de Sistemas")

print(a1.nome, a1.curso)
print(a2.nome, a2.curso)