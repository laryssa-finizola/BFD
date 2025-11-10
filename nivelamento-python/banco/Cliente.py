class Cliente:
    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str, outros: str):
        self.nome: str = nome
        self.email: str = email
        self.cpf: str = cpf
        self.data_nascimento: str = data_nascimento
        self.outros: str = outros  

    def __str__(self) -> str:
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}'