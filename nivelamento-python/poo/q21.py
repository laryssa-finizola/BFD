class Aluno:
    def __init__(self,  n1, n2):
        self.n1 = n1
        self.n2 = n2

    def media(self):
        return (self.n1 + self.n2) / 2

notas = Aluno(5, 10)
print(f"Média do aluno: {notas.media()}")