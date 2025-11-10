class Aluno:
    def __init__(self, nota):
        self.nota = nota
    
    def situacao(self):
        if self.nota >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

a1 = Aluno(8)
print(f"Aluno 1: Nota {a1.nota} - {a1.situacao()}")


a2 = Aluno(5)
print(f"Aluno 2: Nota {a2.nota} - {a2.situacao()}")