class Conta:
    def __init__(self,  saldo = 0):
        self.saldo = saldo

    def  depositar(self, valor):  
        self.saldo += valor

conta = Conta()
print(f"Saldo inicial: {conta.saldo}")

conta.depositar(500)
print(f"Saldo após depósito: {conta.saldo}")