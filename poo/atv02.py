## questão 2: Crie uma Classe Com no mínimo dois objetos e com dois métodos a serem chamados

class Usuario:
    def __init__(self, name, email, password):
        self.name = name,
        self.email = email,
        self.password = password

    # PRIMEIRO MÉTODO: VERIFICA SE A SENHA CRIADA É VÁLIDA (POSSUI PELO MENOS 8 CARACTERES)
    def verifica_senha(self):
        if len(self.password) < 8:
            print(f" Precisa ter pelo menos 8 caracteres.")
            return False
        else:
            print(f"Senha cadastrada.")
            return True
        
    # SEGUNDO MÉTODO: EXIBE AS INFORMAÇÕES DO USUÁRIO
    def exibe_info(self):
        print(f"Nome: {self.name}")
        print(f"Email: {self.email}")

# criação dos objetos da classe Pessoa:
usuario1 = Usuario("Ana", "ana@ex.com", "12345678")
usuario2 = Usuario("Maria", "maria@ex.com", "123456") #senha falha

## verificações 
print("Verificando o primeiro cadastro:")
usuario1.verifica_senha()
usuario1.exibe_info()

print("Verificando o segundo cadastro:")
usuario2.verifica_senha()
usuario2.exibe_info()