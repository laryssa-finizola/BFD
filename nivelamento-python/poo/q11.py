class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

#objetos
f1 = Funcionario("Ana", 2000)
f2 = Funcionario("Maria", 3000)

print(f"Funcionario 1: {f1.nome} - Salario: {f1.salario}")
print(f"Funcionario 2: {f2.nome} - Salario: {f2.salario}")