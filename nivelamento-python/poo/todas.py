class Pessoa:
    def __init__(self, nome):
        self.nome = nome

#objetos
p1 = Pessoa("Laryssa")
p2 = Pessoa("Vinicius")

print(p1.nome)
print(p2.nome)



class Animal:
    def __init__(self, tipo):
        self.tipo = tipo

#objetos
a1 = Animal("Cachorro")
a2 = Animal("Gato")

print(a1.tipo)
print(a2.tipo)


class Carro:
    def __init__(self, estado):
        self.estado = estado

#objetos
fusca = Carro("novo")
ferrari = Carro("usado")

print(fusca.estado)
print(ferrari.estado)


class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

#objetos
c1 = Carro("fusca", "azul")
c2 = Carro("ferrari", "vermelha")

print(f" modelo: {c1.modelo}, cor: {c1.cor}")
print(f" modelo: {c2.modelo}, cor: {c2.cor}")


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

aluno1 = Aluno(nome, nota)
print(f"Aluno: {aluno1.nome}, Nota: {aluno1.nota}")


class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo


conta1 = ContaBancaria(2000)
conta2 = ContaBancaria(50)

print(f"Conta 1 com saldo: {conta1.saldo}")
print(f"Conta 2 com saldo: {conta2.saldo}")


class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def mostrar_saldo(self):
        return f"Saldo: {self.saldo}"

#objetos
conta1 = ContaBancaria(2000)
conta2 = ContaBancaria(50)

#chamada de método
print(conta1.mostrar_saldo())
print(conta2.mostrar_saldo())

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#objetos
produto1 = Produto("mouse", 200)
produto2 = Produto("teclado", 300)
produto3 = Produto("monitor", 800)


#chamada de método
print(f"Nome: {produto1.nome}, Preço: {produto1.preco}")
print(f"Nome: {produto2.nome}, Preço: {produto2.preco}")
print(f"Nome: {produto3.nome}, Preço: {produto3.preco}")


class Computador:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        if self.ligado  == False:
            self.ligado  = True
        else:
            self.ligado = False

computador = Computador()

print(computador.ligado)  

#teste: 
computador.ligar()
print(computador.ligado)


class Lampada:
    def __init__(self):
        self.estado = "Acesa"

    def ligar(self):
        if self.estado  == "Acesa":
            self.estado  = "Apagada"
        else:
            self.estado = "Acesa"

lampada = Lampada()

print(lampada.estado)  

#altera estado
lampada.ligar()
print(lampada.estado) 


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

#objetos
f1 = Funcionario("Ana", 2000)
f2 = Funcionario("Maria", 3000)

print(f"Funcionario 1: {f1.nome} - Salario: {f1.salario}")
print(f"Funcionario 2: {f2.nome} - Salario: {f2.salario}")


class Cachorro:
    def latir(self): 
        print(" Au Au!")

c1 = Cachorro()
c1.latir()



class Celular:
    def __init__(self, bateria):
        self.bateria = bateria

    def carregar(self): 
        if self.bateria < 100:
            self.bateria += 10
        else:
            print("Bateria cheia!")

celular = Celular(50)
print(f"Estado da bateria: {celular.bateria}%")
celular.carregar()
print(f"Estado da bateria: {celular.bateria}%")
celular.carregar()
print(f"Estado da bateria: {celular.bateria}%")



class Livro:    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

l1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling")
l2 = Livro("Matéria escura", " Blake Crouch")


print(f"Título: {l1.titulo}, Autor: {l1.autor}")
print(f"Título: {l2.titulo}, Autor: {l2.autor}")


class Aluno:   
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso



a1 = Aluno("Ana", "Ciência da Computação")
a2 = Aluno("Pedro", "Análise e Desenvolvimento de Sistemas")

print(a1.nome, a1.curso)
print(a2.nome, a2.curso)




class Conta:
    def __init__(self,  saldo = 0):
        self.saldo = saldo

    def  depositar(self, valor):  
        self.saldo += valor

conta = Conta()
print(f"Saldo inicial: {conta.saldo}")

conta.depositar(500)
print(f"Saldo após depósito: {conta.saldo}")





class Conta:
    def __init__(self,  saldo = 200):
        self.saldo = saldo

    def  sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:  
           self.saldo -= valor

conta = Conta()
print(f"Saldo inicial: {conta.saldo}")

conta.sacar(100)
print(f"Saldo após depósito: {conta.saldo}")

#tentando sacar mais do que o disponível: 
conta.sacar(500)





