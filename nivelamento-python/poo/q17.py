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