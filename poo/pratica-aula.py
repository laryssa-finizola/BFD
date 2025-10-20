class Cadastro:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def exibirInformacoes(self):
        return f"Nome: '{self.nome}' | Email: {self.email}"

    def exibirSenha(self):
        return f"Senha: '{self.senha}'"
    
#objetos
cadastro_1 = Cadastro("Laryssa", "laryssa@gmail.com", "12345")
cadastro_2 = Cadastro("Maria", "maria@gmail.com", "12345")


#exibir dados cadastro 1
print("---- Cadastros Efetuados ----")
print(cadastro_1.exibirInformacoes())
print(cadastro_1.exibirSenha())

#exibir dados cadastro 2
print(cadastro_2.exibirInformacoes())
print(cadastro_2.exibirSenha())