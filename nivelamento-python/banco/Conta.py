from Cliente import Cliente


class Conta:
    codigo: int = 1001 # Atributo de classe para gerar números únicos de conta

    def __init__(self, cliente: Cliente):
        self.numero: int = Conta.codigo
        self.cliente: Cliente = cliente
        self.saldo: float = 0.0
        
        Conta.codigo += 1 # Incrementa o código para a próxima conta

    def sacar(self, valor: float) -> None:
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print('Saque efetuado com sucesso.')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            print('Depósito efetuado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def transferir(self, conta_destino: 'Conta', valor: float) -> None:
        if self.saldo >= valor and valor > 0:
            self.sacar(valor)
            conta_destino.depositar(valor)
            print('Transferência realizada com sucesso.')
        else:
            print('Não foi possível realizar a transferência.')
            
    def __str__(self) -> str:
        return (f'Número da Conta: {self.numero}\n'
                f'Cliente: {self.cliente.nome}\n'
                f'CPF: {self.cliente.cpf}\n'
                f'Saldo: R$ {self.saldo:.2f}')