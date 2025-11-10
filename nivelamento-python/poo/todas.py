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


class Pessoa:
    def falar(self): 
        print("Olá, tudo bem?")

p1 = Pessoa()
p1.falar()




class Carro:
    def __init__(self,  marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano do carro: ")

carro = Carro(marca, modelo, ano)
print(f"Carro criado: {carro.marca} {carro.modelo} {carro.ano}")


class Retangulo:
    def __init__(self,  largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura

r1 = Retangulo(5, 10)
print(f"Área do retângulo: {r1.area()}")



class Aluno:
    def __init__(self,  n1, n2):
        self.n1 = n1
        self.n2 = n2

    def media(self):
        return (self.n1 + self.n2) / 2

notas = Aluno(5, 10)
print(f"Média do aluno: {notas.media()}")



class Produto: 
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_desconto(self, porcentagem):
        desconto = self.preco * (porcentagem / 100)
        return self.preco - desconto
    
produto1 = Produto("camisa", 80)
desconto = produto1.calcular_desconto(10)
    
print(f"Nome: {produto1.nome},Preço sem desconto: {produto1.preco}, Preço com desconto: {desconto}")


class Pessoa: 
    def __init__(self, idade):
        self.idade = idade

    def maior_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False
        
p1 = Pessoa(20)
print(f"Pessoa 1 tem maior idade? : {p1.maior_idade()}")

p2 = Pessoa(15)
print(f"Pessoa 2 tem maior idade? : {p2.maior_idade()}")


class Banco: 
    def __init__(self, clientes):
        self.clientes = clientes 

# Objetos
clientes = Banco(["Ana", "Maria", "José"])     

print(f"Clientes do banco: {clientes.clientes}")

class Motor: 
    def __init__(self, ligado=False):
        self.ligado = ligado
    
    def ligar_motor(self):
        self.ligado = True

# Objetos
motor1 = Motor()
motor1.ligar_motor()

print(f"Motor está ligado? {motor1.ligado}")

class Casa: 
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

# Objetos
c1 = Casa("azul", "grande")
c2 = Casa("vermelha", "pequena")

print(f"Casa 1 - Cor: {c1.cor}, Tamanho: {c1.tamanho}")
print(f"Casa 2 - Cor: {c2.cor}, Tamanho: {c2.tamanho}")


class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"Pessoa {self.nome} criada com idade {self.idade}")

# Objetos
p1 = Pessoa("Ana", 30)
p2 = Pessoa("Maria", 25)



class Carro: 
    def __init__(self, estado):
        self.estado = estado

    def mostrar_estado(self):
        return self.estado
    
#objetos 
c1 = Carro("novo")
c2 = Carro("semi novo")

print(f"Estado do carro 1: {c1.mostrar_estado()}")
print(f"Estado do carro 2: {c2.mostrar_estado()}")


class Computador:
    def __init__(self, estado):
        self.estado = estado
    
    def info(self):
        if self.estado == True:
            return "computador ligado"
        else:
            return "computador desligado"

teste1 = Computador(True)
print(teste1.info())

teste2 = Computador(False)
print(teste2.info())


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