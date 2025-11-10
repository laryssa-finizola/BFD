class Conta:
    def __init__(self,  saldo = 0):
        self.saldo = saldo

    def  depositar(self, valor):  
        self.saldo += valor

conta = Conta()
print(f"Saldo inicial: {conta.saldo}")

conta.depositar(700)
print(f"Saldo após primeiro depósito: {conta.saldo} reais")

conta.depositar(77)
print("Saldo após segundo depósito: ", conta.saldo, "reais")