class Cadastro:
    def __init__(self, nome, idade, telefone, endereco, cidade):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade

pessoaA = Cadastro("Laryssa", 23, "83999229922", "rua maria joão", "campina grande")
pessoaB = Cadastro("Maria", 35, "83912131415", "rua joão maria", "campina grande")


print(f"\nOlá {pessoaA.nome}, obrigada por se cadastrar")

print(f"Informações adicionais sobre {pessoaA.nome}: \nIdade = {pessoaA.idade}\nTelefone = {pessoaA.telefone} \nEndereço = {pessoaA.endereco} \nCidade = {pessoaA.cidade}")