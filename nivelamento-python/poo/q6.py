class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo


conta1 = ContaBancaria(2000)
conta2 = ContaBancaria(50)

print(f"Conta 1 com saldo: {conta1.saldo}")
print(f"Conta 2 com saldo: {conta2.saldo}")