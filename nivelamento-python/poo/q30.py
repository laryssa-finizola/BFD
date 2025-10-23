class Aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def media (nota1, nota2):
        media = (nota1 + nota2)/2
        return media
    
    def situacao(media):
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")