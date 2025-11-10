# crie uma classe funcionario com o atributo nome e salario
#  imprima o nome e salario de dois funcionarios


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario 

#objetos: 
f1 = Funcionario("Ana", 3000)
f2 = Funcionario("Maria", 2500)  

print(f"Primeiro funcionário: {f1.nome}\nSalário: {f1.salario}")
print(f"Segundo funcionário: {f2.nome}\nSalário: {f2.salario}")

       