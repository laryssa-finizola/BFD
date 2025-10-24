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